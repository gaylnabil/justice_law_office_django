# -*- coding: utf-8 -*-
###################################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#    Copyright (C) 2018-TODAY Cybrosys Technologies(<http://www.cybrosys.com>).
#    Author: cybrosys(<https://www.cybrosys.com>)
#
#    This program is free software: you can modify
#    it under the terms of the GNU Affero General Public License (AGPL) as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###################################################################################
import pytz
import sys
from datetime import datetime, timedelta
import logging
import binascii
import pathlib

from . import zklib
from .zkconst import *
from struct import unpack
from odoo import api, fields, models
from odoo import _
from odoo.exceptions import UserError, ValidationError
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT

_logger = logging.getLogger(__name__)

class HrAttendance(models.Model):
    _inherit = 'hr.attendance'   
    device_id = fields.Char(string='Biometric Device ID')

class ZkMachine(models.Model):
    _name = 'zk.machine'
    
    name = fields.Char(string='Machine IP', required=True)
    port_no = fields.Integer(string='Port No', required=True)
    address_id = fields.Many2one('res.partner', string='Working Address')
    company_id = fields.Many2one('res.company', string='Company', default=lambda self: self.env.user.company_id.id)

    @api.multi
    def device_connect(self, zk):
        command = CMD_CONNECT
        command_string = ''
        chksum = 0
        session_id = 0
        reply_id = -1 + USHRT_MAX
        buf = zk.createHeader(command, chksum, session_id,
                              reply_id, command_string)
        zk.zkclient.sendto(buf, zk.address)
        try:
            zk.data_recv, addr = zk.zkclient.recvfrom(1024)
            zk.session_id = unpack('HHHH', zk.data_recv[:8])[2]
            command = unpack('HHHH', zk.data_recv[:8])[0]
            if command == 2000:
                conn = True
            else:
                conn = False
        except:
            conn = False
        return conn
    
    @api.multi
    def clear_attendance(self):
        for info in self:
            try:
                machine_ip = info.name
                port = info.port_no
                zk = zklib.ZKLib(machine_ip, port)
                conn = self.device_connect(zk)
                if conn:
                    zk.enableDevice()
                    clear_data = zk.getAttendance()
                    if clear_data:
                        zk.clearAttendance()
                        self._cr.execute("""delete from zk_machine_attendance""")
                    else:
                        raise UserError(_('Unable to get the attendance log, please try again later.'))
                else:
                    raise UserError(_(info.name)) 
            except:
                raise 

    def getSizeUser(self, zk):
        """Checks a returned packet to see if it returned CMD_PREPARE_DATA,
        indicating that data packets are to be sent

        Returns the amount of bytes that are going to be sent"""
        command = unpack('HHHH', zk.data_recv[:8])[0]
        if command == CMD_PREPARE_DATA:
            size = unpack('I', zk.data_recv[8:12])[0]
            return size
        else:
            return False

#    def zkgetuser(self, zk):
#        """Start a connection with the time clock"""
#        command = CMD_USERTEMP_RRQ
#        command_string = '\x05'
#        chksum = 0
#        session_id = zk.session_id
#        reply_id = unpack('HHHH', zk.data_recv[:8])[3]
#
#        buf = zk.createHeader(command, chksum, session_id, reply_id, command_string)
#        zk.zkclient.sendto(buf, zk.address)
#        try:
#            zk.data_recv, addr = zk.zkclient.recvfrom(1024)
#
#            if self.getSizeUser(zk):
#                bytes = self.getSizeUser(zk)
#
#                while bytes > 0:
#                    data_recv, addr = zk.zkclient.recvfrom(1032)
#                    zk.userdata.append(data_recv)
#                    bytes -= 1024
#
#                zk.session_id = unpack('HHHH', zk.data_recv[:8])[2]
#                data_recv = zk.zkclient.recvfrom(8)
#
#            users = {}
#            if len(zk.userdata) > 0:
#                userdata = zk.userdata[0]
#                userdata = userdata[11:]
#                while len(userdata) > 72:
#                    uid, role, password, name, userid = unpack('2s2s8s28sx31s', userdata.ljust(72)[:72])
#                    uid = int(binascii.hexlify(uid), 16)
#                    # Clean up some messy characters from the user name
#                    password = password.split(b'\x00', 1)[0]
#                    password = str(password.strip(b'\x00|\x01\x10x|\x000').decode('utf-8'))
#                    # uid = uid.split('\x00', 1)[0]
#                    userid = str(userid.strip(b'\x00|\x01\x10x|\x000|\x9aC').decode('utf-8'))
#                    name = name.split(b'\x00', 1)[0].decode('utf-8')
#                    if name.strip() == "":
#                        name = uid
#                    users[uid] = (userid, name, int(binascii.hexlify(role), 16), password)
#                    userdata = userdata[72:]
#            return users
#        except:
#            return False

    def zkgetuser(self, zk):
        """Start a connection with the time clock"""
        command = CMD_USERTEMP_RRQ
        command_string = '\x05'
        chksum = 0
        session_id = zk.session_id
        reply_id = unpack('HHHH', zk.data_recv[:8])[3]

        buf = zk.createHeader(command, chksum, session_id,
            reply_id, command_string)
        zk.zkclient.sendto(buf, zk.address)
        #print buf.encode("hex")
        try:
            zk.data_recv, addr = zk.zkclient.recvfrom(1024)
            
            if self.getSizeUser(zk):
                bytes = self.getSizeUser(zk)
                
                while bytes > 0:
                    data_recv, addr = zk.zkclient.recvfrom(1032)
                    zk.userdata.append(data_recv)
                    bytes -= 1024
                
                zk.session_id = unpack('HHHH', zk.data_recv[:8])[2]
                data_recv = zk.zkclient.recvfrom(8)
            
            users = {}
            if len(zk.userdata) > 0:
                # The first 4 bytes don't seem to be related to the user
                for x in range(len(zk.userdata)):
                    if x > 0:
                        zk.userdata[x] = zk.userdata[x][8:]
                
                userdata = b''.join(zk.userdata)
                userdata = userdata[11:]
                
                while len(userdata) > 72:
                    
                    uid, role, password, name, userid = unpack( '2s2s8s28sx31s', userdata.ljust(72)[:72] )
                    uid = int(uid.hex(), 16)
                    #print ("uid : ", uid)
                    # Clean up some messy characters from the user name
                    password = password.split(b'\x00', 1)[0]
                    password = str(password.strip(b'\x00|\x01\x10x'), errors='ignore')
                    #print ("password : ",password)
                    userid = userid.strip(b'\x00|\x01\x10x')
                    
                    userid = userid.decode('utf-8', 'ignore')
                    
                    #print ("userid : ", userid)
                    name = name.split(b'\x00')[0]
                    #print ("name : ", name.decode())
                    name = name.decode()
                    if name.strip() == "":
                        name = uid
                    
                    users[uid] = (userid, name, int( role.hex(), 16 ), password)
                    #print("%d, %s, %s, %s, %s" % (uid, userid, name, int( role.hex(), 16 ), password))
                    userdata = userdata[72:]
                    
            return users
        except:
            zk.enableDevice()
            zk.disconnect()
            raise
            return False


    def get_delay(self, resource, date_check, is_checked_out):
    
        """ 
        :author  : Nabil GAYL
        :function get_delay: Getting a values of delay or early out time
        :param resource: resource.calendar
        :param date_check: datetime
        :param is_checked_out: boolean
        
        """
        delay = 0
        hour_start = 0
        hour_end = 0
        day_of_week = date_check.weekday()
        for res in resource.attendance_ids:
            if day_of_week == int(res.dayofweek):
                time = date_check.hour + date_check.minute / 60.0
                hour_start = res.hour_from
                hour_end = res.hour_to
                delay = (hour_end - time) if is_checked_out == True else (time - hour_start)

                #_logger.info("HrAttendance - Calender => dayofweek Type: {}, hour from : {}, hour to : {}, Date : {}, Day of Week : {}, Delay : {}, is_checked_out : {}.".format(type(res.dayofweek), res.hour_from, res.hour_to, date_check, day_of_week, delay, is_checked_out))
                break
        return (hour_start, delay, hour_end)   

    @api.model
    def cron_download(self):
        machines = self.env['zk.machine'].search([])
        for machine in machines :
            confirmed = machine.download_attendance()
        
    @api.multi
    def download_attendance(self):
        _logger.info("++++++++++++Cron Executed++++++++++++++++++++++")

        zk_attendance = self.env['zk.machine.attendance']
        att_obj = self.env['hr.attendance']

        """ Getting array of worktime objects """
        work_obj = self.env['hr.worktime']
        
        # work_obj.create({'employee_id': 2, 'min_check_in': "", 'max_check_in': ""})
        # work_obj.create({'employee_id': 3, 'min_check_in': "", 'max_check_in': ""})

        for info in self:
            machine_ip = info.name
            port = info.port_no
            zk = zklib.ZKLib(machine_ip, port)
            conn = self.device_connect(zk)
            if conn:
                zk.disableDevice()
                user = self.zkgetuser(zk)
                
                command = CMD_ATTLOG_RRQ
                command_string = ''
                chksum = 0
                session_id = zk.session_id
                reply_id = unpack('HHHH', zk.data_recv[:8])[3]
                buf = zk.createHeader(command, chksum, session_id,
                                      reply_id, command_string)
                zk.zkclient.sendto(buf, zk.address)
                try:
                    zk.data_recv, addr = zk.zkclient.recvfrom(1024)
                    command = unpack('HHHH', zk.data_recv[:8])[0]
                    if command == CMD_PREPARE_DATA:
                        size = unpack('I', zk.data_recv[8:12])[0]
                        zk_size = size
                    else:
                        zk_size = False
                    if zk_size:
                        bytes = zk_size
                        while bytes > 0:
                            data_recv, addr = zk.zkclient.recvfrom(1032)
                            zk.attendancedata.append(data_recv)
                            bytes -= 1024
                        zk.session_id = unpack('HHHH', zk.data_recv[:8])[2]
                        data_recv = zk.zkclient.recvfrom(8)
                    attendance = []
                    if len(zk.attendancedata) > 0:
                        # The first 4 bytes don't seem to be related to the user
                        for x in range(len(zk.attendancedata)):
                            if x > 0:
                                zk.attendancedata[x] = zk.attendancedata[x][8:]
                        attendancedata = b''.join(zk.attendancedata) 
                        attendancedata = attendancedata[14:] 
                        #while len(attendancedata) > 0:
                        while len(attendancedata):
                            uid, state, timestamp, space = unpack('24s1s4s11s', attendancedata.ljust(40)[:40])
                            pls = unpack('c', attendancedata[29:30])
                            uid = uid.split(b'\x00', 1)[0].decode('utf-8')
                            tmp = ''
                            for i in reversed(range(int(len(binascii.hexlify(timestamp)) / 2))):
                                tmp += binascii.hexlify(timestamp).decode('utf-8')[i * 2:(i * 2) + 2] 

                                
                            attendance.append((uid, int(binascii.hexlify(state), 16),
                                               decode_time(int(tmp, 16)), unpack('HHHH', space[:8])[0]))
                            
                            attendancedata = attendancedata[40:]
                except Exception as e:
                    _logger.info("++++++++++++Exception++++++++++++++++++++++", e)
                    attendance = False
                
                current_dir = pathlib.Path(__file__).parent
                filename = str(current_dir) + "/nga_da_cron_download.log"
                _logger.info("NGA  => add_logs_to_file => filename : {}".format(filename))

                file = open(filename,"a+")
                file.write("{} => Begin Cron Download... \n".format(datetime.now()))
                file.write("Attendance Array Length : {}  \n".format(len(attendance)))
                file.close()

                if attendance:

                    for each in attendance:
                    
                        atten_time = each[2]
                        atten_time = datetime.strptime(
                            atten_time.strftime('%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S')
                            
                        user_tz = pytz.timezone(self.env.context.get('tz') or 'UTC')

                        atten_time = pytz.utc.localize(atten_time, is_dst=None).astimezone(user_tz)

                        #time = atten_time
                        #time= atten_time.timetz();
                        #time = atten_time.hour + atten_time.minute / 60.0
                        #_logger.info("tztime => {}; Type => {}".format(time, type(time)))

                        # local_tz = pytz.timezone(
                        #     self.env.user.partner_id.tz or self.env.context.get('tz'))
                        #********************************************************
                        # local_tz = pytz.timezone(
                        #     self.env.user.partner_id.tz or 'GMT')

                        # local_dt = local_tz.localize(atten_time, is_dst=None)
                        # utc_dt = local_dt.astimezone(pytz.utc)

                        # utc_dt = utc_dt.strftime("%Y-%m-%d %H:%M:%S")
                        # atten_time = datetime.strptime(
                        #     utc_dt, "%Y-%m-%d %H:%M:%S")
                        #********************************************************
                        time  = datetime.strftime(atten_time, "%H:%M:%S")

                        atten_time = fields.Datetime.to_string(atten_time)
                        
                        _logger.info("atten_time => {}".format(atten_time))
                        skip = 0
                        line = 0
                        if user:
                            for uid in user:
                                if user[uid][0] == str(each[0]):
                                    get_user_id = self.env['hr.employee'].search(
                                        [('device_id', '=', str(each[0]))])
                                    if get_user_id:
                                        
                                        resource = get_user_id.resource_calendar_id

                                        duplicate_atten_ids = zk_attendance.search(
                                            [('device_id', '=', str(each[0])), ('punching_time', '=', atten_time), ('timing', '=', time)])
                                        #_logger.info("duplicate_atten_ids => Device ID : {}, Name : {}, Punch Type : {}, punching_time : {}, Length : {}".format(each[0], get_user_id.name, each[3], atten_time, len(duplicate_atten_ids)))
                                        if duplicate_atten_ids:
                                            skip += 1
                                            continue
                                        else: 
                                            line += 1
                                            zk_attendance.create({'employee_id': get_user_id.id,
                                                                  'device_id': each[0],
                                                                  'attendance_type':str(each[3]),
                                                                  'punch_type': repr(each[1]),
                                                                  'punching_time': atten_time,
                                                                  'timing' : time,
                                                                  'address_id': info.address_id.id})

                                            att_var = att_obj.search([('employee_id', '=', get_user_id.id),
                                                                      ('check_out', '=', False)])

                                            date_in = fields.Datetime.from_string(atten_time)

                                            #_logger.info("download_attendance => attendance_type : {}, Punch Type : {}, punching_time : {}".format(each[3], each[1], atten_time))
                                            if each[1] != 101: #check-in
                                                #*****************************************************************
                                                day_of_week = date_in.weekday()
                                                
                                                time_in = datetime.strftime(date_in, "%H:%M:%S")

                                                data_exists = work_obj.search([('employee_id', '=', get_user_id.id), ('min_check_in', '=', date_in)])

                                                #_logger.info("Zk Machine Table Exist => {}, Data Exists : {}".format(data_exists, len(data_exists)))

                                                if len(data_exists) == 0:
                                                    work_obj.create({'employee_id': get_user_id.id, 'day_name': day_of_week , 'min_check_in': date_in, 'min_check_in_time' : time_in})  
                                                    #data_exists = work_obj.create({'employee_id': get_user_id.id, 'day_name': day_of_week , 'min_check_in': date_in, 'min_check_in_time' : time_in})  
                                                    data_exists = work_obj.search([('employee_id', '=', get_user_id.id), ('min_check_in', '=', date_in)])
                                                else:
                                                    date_in = datetime.strptime("{} {}".format(data_exists[0].min_check_in, data_exists[0].min_check_in_time), "%Y-%m-%d %H:%M:%S") 
                                                    
                                                delay_info = self.get_delay(resource, date_in, False)

                                                data_exists.write({'hour_start' : delay_info[0], 'delay' :  delay_info[1], 'hour_end' :  delay_info[2]})   

                                                #*****************************************************************

                                                if not att_var:
                                                    att_obj.create({'employee_id': get_user_id.id,'check_in': atten_time})
                                                    

                                            #if each[3] == 1: #check-out
                                            else:
                                                
                                                #*****************************************************************
                                                date_out = fields.Datetime.from_string(atten_time)
                                                time_in = datetime.strftime(date_in, "%H:%M:%S")
                                                time_out = datetime.strftime(date_out, "%H:%M:%S")
                                                data_exists = work_obj.search([('employee_id', '=', get_user_id.id), ('min_check_in', '=', date_in)])
                                                _logger.info("check-out =>  : {}, data_exists : {}".format(atten_time, len(data_exists)))
                                                if len(data_exists) > 0:
                                                    # resource = get_user_id.resource_calendar_id
                                                    delay_info = self.get_delay(resource, date_out, True)
                                                    #data_exists.write({'max_check_out': date_out, 'max_check_out_time': time_out})  
                                                    data_exists.write({'max_check_out': date_out, 'max_check_out_time': time_out, 'early_out' : delay_info[1]})  
                                                    _logger.info("Nabil GAYl Date Out => Employee Name : {}, Check out : {}, early out : {}".format(get_user_id.name, date_out,delay_info[1]))
                                                #*****************************************************************
                                                if len(att_var) == 1:
                                                    att_var.write({'check_out': atten_time})

                                                    #_logger.info("download_attendance => att_var : {}, Check out : {}".format(att_var, atten_time))
                                                else:
                                                    att_var1 = att_obj.search([('employee_id', '=', get_user_id.id)])
                                                    #if len(att_var1) > 0:
                                                    if att_var1:
                                                        _logger.info("download_attendance => att_var1 : {}, Check out : {}, length : {}".format(att_var1, atten_time, len(att_var1)))
                                                        att_var1[-1].write({'check_out': atten_time})
                                    else:
                                        line += 1
                                        employee = self.env['hr.employee'].create(
                                            {'device_id': str(each[0]), 'name': user[uid][1]})
                                        zk_attendance.create({'employee_id': employee.id,
                                                              'device_id': each[0],
                                                              'attendance_type':str(each[3]),
                                                              'punch_type': repr(each[1]),
                                                              'punching_time': atten_time,
                                                              'timing' : time,
                                                              'address_id': info.address_id.id})
                                        att_obj.create({'employee_id': employee.id,
                                                        'check_in': atten_time})

                                        #*****************************************************************
                                        resource = employee.resource_calendar_id

                                        date_in = fields.Datetime.from_string(atten_time)
                                        day_of_week = date_in.weekday()

                                        time_in = datetime.strftime(date_in, "%H:%M:%S")

                                        data_exists = work_obj.search([('employee_id', '=', employee.id), ('min_check_in', '=', date_in)])

                                        _logger.info("Condition Else => {}, Data Exists : {}".format(data_exists, len(data_exists)))

                                        if len(data_exists) == 0:
                                            work_obj.create({'employee_id': employee.id, 'day_name': day_of_week , 'min_check_in': date_in, 'min_check_in_time' : time_in})  
                                            data_exists = work_obj.search([('employee_id', '=', employee.id), ('min_check_in', '=', date_in)])
                                        else:
                                            date_in = datetime.strptime("{} {}".format(data_exists[0].min_check_in, data_exists[0].min_check_in_time), "%Y-%m-%d %H:%M:%S") 
                                            
                                        delay_info = self.get_delay(resource, date_in, False)

                                        data_exists.write({'hour_start' : delay_info[0], 'delay' :  delay_info[1], 'hour_end' :  delay_info[2]})   

                                        _logger.info("Condition Else 2 : {} Type : {}=> ".format(date_in, type(date_in)))
                                        
                                        #*****************************************************************
                    
                                else:
                                    pass
                     
                    zk.enableDevice()
                    zk.disconnect()

                    file = open(filename,"a+")
                    file.write("Skip : {}\n".format(skip))
                    file.write("line pass : {}\n".format(line))
                    file.write("{} => Download complet.\n".format(datetime.now()))
                    file.write("****************************************************************\n")
                    file.close()

                    return True
                else:
                    zk.enableDevice()
                    zk.disconnect()

                    file = open(filename,"a+")
                    file.write("Skip : {}\n".format(skip))
                    file.write("line pass : {}\n".format(line))
                    file.write("{} => Error Unable to get the attendance log. \n".format(datetime.now()))
                    file.write("****************************************************************\n")
                    file.close()

                    raise UserError(_('Unable to get the attendance log, please try again later.'))
            else:
                zk.enableDevice()
                zk.disconnect()

                file = open(filename,"a+")
                file.write("Skip : {}\n".format(skip))
                file.write("line pass : {}\n".format(line))
                file.write("{} => Error. \n".format(datetime.now()))
                file.write("****************************************************************\n")
                file.close()

                raise 


	

-- local lunit = require("lunit")
-- local CRC = require("crc16.crc16")
-- print("lunit 1 => " .. lunit.assert_equal(0xBB3D, CRC.crc16({"1", "2", "3", "4", "5", "6", "7", "8", "9"})))
-- print("lunit 2 => " .. lunit.assert_equal(0xBB3D, CRC.crc16({49, 50, 51, 52, 53, 54, 55, 56, 57})))
-- print("lunit 3 => " .. lunit.assert_equal(0xE9D9, CRC.crc16("abcdefg")))
-- print("lunit 4 => " .. lunit.assert_equal(0x0F65, CRC.crc16("0123456789ABCDEF")))
-- print("lunit 5 => " .. lunit.assert_equal(0x0F65, CRC.crc16({"0123456789", "ABCDEF"})))
-- print("lunit 6 => " .. lunit.assert_equal(0xBB3D, CRC.crc16("123456789")))
-- print("CRC connect : *************************************************************************")
-- print(" CRC Connect 1 => " .. lunit.assert_equal(0x8fd7, CRC.crc16({0x01, 0x76, 0x04, 0x00, 0x00, 0x00, 0x00, 0x00}))) -- request
-- print(" CRC Connect 2 => " ..
--           lunit.assert_equal(0x3320, CRC.crc16(string.char(0x01, 0xc8, 0x04, 0x00, 0xd6, 0xcd, 0x00, 0x00)))) -- response
-- print(" CRC Connect 3 => " .. lunit.assert_equal(0x47c8, CRC.crc16({0x01, 0xc8, 0x04, 0x00, 0x54, 0xf1, 0x00, 0x00}))) -- response
-- print("CRC real log : *************************************************************************")
-- print(" real log lunit 1 => " ..
--           lunit.assert_equal(0xbf72, CRC.crc16(string.char(0x01, 0x0b, 0x04, 0x00, 0x78, 0xe5, 0x02, 0x00)))) -- request
-- print(" real log lunit 2 => " .. lunit.assert_equal(0xcd2c,
--           CRC.crc16({0x01, 0xc8, 0x14, 0x00, 0x78, 0xe5, 0x02, 0x00, 0x03, 0x00, 0x00, 0x00, 0x11, 0x00, 0x00, 0x00,
--                      0x00, 0x01, 0xff, 0x00, 0x00, 0x33, 0x75, 0x21}))) -- response
-- print(" real log lunit 2 => " .. lunit.assert_equal(0x4f24,
--           CRC.crc16(string.char(0x01, 0xc8, 0x14, 0x00, 0x54, 0xf1, 0x02, 0x00, 0x03, 0x00, 0x00, 0x00, 0x11, 0x00,
--                         0x00, 0x00, 0x00, 0x01, 0xff, 0x00, 0xda, 0x3e, 0x75, 0x21)))) -- response
-- print(" real log lunit 3 => " .. lunit.assert_equal(0xf687, CRC.crc16({0x01, 0x0b, 0x04, 0x00, 0x3e, 0xe3, 0x02, 0x00}))) -- request
-- t = {}
-- s = "from=world, to=Lua"
-- for k, v in string.gmatch(s, "(%w+)=(%w+)") do
--     t[k] = v
-- end
-- print("NGA table :")
-- print(table.concat(t, ", "))
local socket = require("socket") -- for having a sleep function
local C3 = require("c3.c3")

local c3_ip = "10.220.1.5"
if c3_ip then
    C3.setDebug(false)

    print("Connecting to " .. c3_ip .. " ... ")
    local connected, err = C3.connect(c3_ip)
    if connected then
        print("Connected **************************************** ")
        -- print("SessionId: " .. C3.getSessionId())
        print("Press Ctrl-C to stop.")

        local parameters = C3.getDeviceParameters({"~SerialNumber", "LockCount", "ReaderCount", "AuxInCount",
                                                   "AuxOutCount", "DateTime"})
        print("Parametres :")
        print(parameters)

        -- C3.disconnect()

        print("SessionId: " .. C3.getSessionId())
        print("Disconnected.")
    else
        error("Connection failed:" .. err, 0)
    end
end

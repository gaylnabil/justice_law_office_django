/*
 Navicat Premium Data Transfer

 Source Server         : PostgreSQL Connection
 Source Server Type    : PostgreSQL
 Source Server Version : 120003
 Source Host           : localhost:5432
 Source Catalog        : allo
 Source Schema         : public

 Target Server Type    : PostgreSQL
 Target Server Version : 120003
 File Encoding         : 65001

 Date: 04/02/2021 16:17:15
*/


-- ----------------------------
-- Sequence structure for attorney_groups_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."attorney_groups_id_seq";
CREATE SEQUENCE "public"."attorney_groups_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for attorney_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."attorney_id_seq";
CREATE SEQUENCE "public"."attorney_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for attorney_user_permissions_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."attorney_user_permissions_id_seq";
CREATE SEQUENCE "public"."attorney_user_permissions_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for auth_group_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."auth_group_id_seq";
CREATE SEQUENCE "public"."auth_group_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for auth_group_permissions_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."auth_group_permissions_id_seq";
CREATE SEQUENCE "public"."auth_group_permissions_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for auth_permission_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."auth_permission_id_seq";
CREATE SEQUENCE "public"."auth_permission_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for category_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."category_id_seq";
CREATE SEQUENCE "public"."category_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for city_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."city_id_seq";
CREATE SEQUENCE "public"."city_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for comment_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."comment_id_seq";
CREATE SEQUENCE "public"."comment_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for django_admin_log_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."django_admin_log_id_seq";
CREATE SEQUENCE "public"."django_admin_log_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for django_content_type_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."django_content_type_id_seq";
CREATE SEQUENCE "public"."django_content_type_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for django_migrations_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."django_migrations_id_seq";
CREATE SEQUENCE "public"."django_migrations_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for question_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."question_id_seq";
CREATE SEQUENCE "public"."question_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for schedule_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."schedule_id_seq";
CREATE SEQUENCE "public"."schedule_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for subcomment_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."subcomment_id_seq";
CREATE SEQUENCE "public"."subcomment_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Table structure for attorney
-- ----------------------------
DROP TABLE IF EXISTS "public"."attorney";
CREATE TABLE "public"."attorney" (
  "id" int4 NOT NULL DEFAULT nextval('attorney_id_seq'::regclass),
  "password" varchar(128) COLLATE "pg_catalog"."default" NOT NULL,
  "last_login" timestamptz(6),
  "is_superuser" bool NOT NULL,
  "username" varchar(150) COLLATE "pg_catalog"."default" NOT NULL,
  "first_name" varchar(150) COLLATE "pg_catalog"."default" NOT NULL,
  "last_name" varchar(150) COLLATE "pg_catalog"."default" NOT NULL,
  "email" varchar(254) COLLATE "pg_catalog"."default" NOT NULL,
  "is_staff" bool NOT NULL,
  "is_active" bool NOT NULL,
  "date_joined" timestamptz(6) NOT NULL,
  "type" varchar(50) COLLATE "pg_catalog"."default",
  "address" varchar(255) COLLATE "pg_catalog"."default",
  "sex" varchar(1) COLLATE "pg_catalog"."default",
  "building" varchar(255) COLLATE "pg_catalog"."default",
  "neighborhood" varchar(255) COLLATE "pg_catalog"."default",
  "indication" varchar(255) COLLATE "pg_catalog"."default",
  "city" varchar(150) COLLATE "pg_catalog"."default",
  "zip_code" int4,
  "tel" varchar(255) COLLATE "pg_catalog"."default",
  "gsm" varchar(255) COLLATE "pg_catalog"."default",
  "presentation" text COLLATE "pg_catalog"."default",
  "education" text COLLATE "pg_catalog"."default",
  "experience" text COLLATE "pg_catalog"."default",
  "skill" text COLLATE "pg_catalog"."default",
  "rib" varchar(255) COLLATE "pg_catalog"."default",
  "instagram" varchar(255) COLLATE "pg_catalog"."default",
  "youtube" varchar(255) COLLATE "pg_catalog"."default",
  "facebook" varchar(255) COLLATE "pg_catalog"."default",
  "web" varchar(255) COLLATE "pg_catalog"."default",
  "video" varchar(200) COLLATE "pg_catalog"."default",
  "profile_image" varchar(255) COLLATE "pg_catalog"."default"
)
;

-- ----------------------------
-- Records of attorney
-- ----------------------------
INSERT INTO "public"."attorney" VALUES (1, 'pbkdf2_sha256$216000$ADnPv07c16jB$OMzEw7cBbDq/uPOgOr4CoWsD07rLHb97GISBWyZZTbM=', '2020-12-02 16:27:12.322592+01', 'f', 'fadisamir', 'Samir', 'FADI', 'sakazaki.services@gmail.com', 't', 't', '2020-11-24 09:38:40.711765+01', 'attorney', '101, Boulevard abdelmoumen', 'H', '196 imm, 3éme étage, apt 15', 'Maarif', NULL, 'Casablanca', 20010, '+212679396337', '+212679396337', 'A presentation is the process of communicating a topic to an audience. It is typically a demonstration, introduction, lecture, or speech meant to inform, persuade, inspire, motivate, or to build good will or to present a new idea or product.[1] The term can also be used for a formal[2] or ritualized introduction or offering, as with the presentation of a debutante. Presentations in certain formats are also known as keynote[3] address.', 'Get a learning boost with thousands of worksheets, games, lesson plans, and more from our library of printable and digital resources for preschool, kindergarten', '(the process of getting) knowledge or skill from doing, seeing, or feeling things:

Do you have any experience of working with kids? (= Have you ever worked with them?)

The best way to learn is by experience (= by doing things).

I know from experience that Tony never keeps his promises.

I don''t think she has the experience for the job (= enough knowledge and skill for it).

In my experience, people generally smile back if you smile at them.

The experience of pain (= what pain feels like) varies from one person to another.', 'Compétences professionnelle : définition

Qu’est ce qu’une compétence professionnelle ? C’est un savoir-faire ou un savoir-être qui permet de créer de la valeur ajoutée.



Exemple de savoir-faire : à partir d’ingrédients de base, un pâtissier va créer des gateaux, qu’il pourra vendre plus cher que le prix des ingrédients.



Exemple de savoir-être : par la qualité de son accueil (sourire, écoute, disponibilité, réactivité) une employée de réception d’un hôtel mettra les clients dans un bon état d’esprit et fera de leur séjour un moment agréable.



A noter que parfois, la différence entre savoir-être et qualité personnelle est ténue. Par exemple,  » être clair dans sa façon de communiquer  » est à la fois un savoir-être et une qualité personnelle. Peu importe dans quel case on range de concept, l’important, c’est la plus-value pour l’employeur.



Ci-dessous, découvrez une liste de 12 types de compétences professionnelles, illustrées par des exemples dans différents domaines.', NULL, 'https://www.instagram.com/miss.rover/', 'https://www.youtube.com/channel/UCTZRcDjjkVajGL6wd76UnGg', 'https://www.facebook.com/ayoub.machache', NULL, 'https://www.youtube.com/watch?v=rDGqCeryAaY&ab_channel=DennisIvy', 'uploads/2020/12/02/noble.jpg');
INSERT INTO "public"."attorney" VALUES (2, 'pbkdf2_sha256$216000$ADnPv07c16jB$OMzEw7cBbDq/uPOgOr4CoWsD07rLHb97GISBWyZZTbM=', NULL, 'f', 'morabiamal', 'Amal', 'MORABI', 'morabi.amal@gmail.com', 't', 't', '2020-11-25 19:38:40.711765+01', 'attorney', NULL, 'F', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "public"."attorney" VALUES (3, 'pbkdf2_sha256$216000$ADnPv07c16jB$OMzEw7cBbDq/uPOgOr4CoWsD07rLHb97GISBWyZZTbM=', NULL, 'f', 'fadidounia', 'Dounia', 'FADI', 'dounia.fadi@gmail.com', 't', 't', '2020-11-26 22:02:10.711765+01', 'attorney', NULL, 'F', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "public"."attorney" VALUES (4, 'pbkdf2_sha256$216000$ADnPv07c16jB$OMzEw7cBbDq/uPOgOr4CoWsD07rLHb97GISBWyZZTbM=', '2021-02-04 11:47:05.650536+01', 'f', 'daly', 'kamal', 'DALY', 'daly2020@outlook.com', 't', 't', '2020-11-26 23:52:10.711765+01', 'attorney', NULL, 'H', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "public"."attorney" VALUES (5, 'pbkdf2_sha256$216000$ADnPv07c16jB$OMzEw7cBbDq/uPOgOr4CoWsD07rLHb97GISBWyZZTbM=', '2021-02-04 14:09:54.70508+01', 't', 'gaylnabil', 'Nabil', 'GAYL', 'gaylnabil@gmail.com', 't', 't', '2020-11-23 13:16:12.711765+01', 'attorney', 'AL AZHAR2 GH 19', 'H', 'imm 130 CASABLANCA 20230 Appt. 20', NULL, NULL, 'Casablanca', 20010, '+212522989404', '+212679396337', 'Mon nom est [ton prénom et ton nom] et je travaille actuellement comme [poste que tu occupes] au sein de la société [nom de l’entreprise pour laquelle tu travailles]. Par la présente, je souhaite vous faire part de mon intérêt pour le poste de [nom du poste auquel tu postules], car il correspond exactement aux missions que j’ai pu réaliser au cours de mes dernières expériences professionnelles.', 'Nous avons choisi de nous inscrire dans cette démarche de plan de formation dans un souci

d’améliorer la qualité de notre service.

Les objectifs généraux assignés en interne sont les suivants :

- mettre les différents intervenants sur un même niveau de compétences

- mettre en évidence les manques, les besoins et y remédier

- amener une remise en question de chacun à son niveau', 'Organisation d’événements : lancement de produits, forums, foire commerciales, salons

Organisation de rencontres : séminaires, formations, présentations à la presse, aux actionnaires

Organisation d’espace : restructuration de bureaux, déménagement

Gestions de projets : constitution d’équipe, suivi de l’avancement

Organisation personnelle, productivité : respect des délais, savoir gérer son temps, les priorités

Savoir organiser des données, mener des études quantitatives

Savoir partir d’un concept pour réaliser un projet

Compétence entrepreneuriale', ' Programming Web:

 Full Stack:

- Front End: HTML, CSS, CSS3, JavaScript, jQuery, Bootstrap Framework.

- Back End: Python, PHP MySQL, Frameworks (Django Symfony, LARAVEL), JAVA J2EE.

- Search Engine Optimization, Web Marketing.

 Programming Desktop: VB.NET, ADO.NET, C#, JAVA, Python.

 Databases: SQL Server, MySQL, PostgreSQL, Access, Excel.

 Analyze and conception: Merise, Uml.

 Integrated Development Environment: Visual Studio 2017/2019,, Visual Studio Code,

PyCharm.

 IT Support & Networking:

- Diagnosis of desktop, application, networking and operating System issues.

- Installing and upgrading hardware and IT equipment

- Troubleshooting PC’s, laptops and mobile devices.

- Supporting: Windows 7/8/10 and Windows Server.

- Installation and configuration of Anti-Virus products, DNS/DHCP, TCP/IP, Ethernet, wireless

router and Firewall Configurations.', NULL, 'https://www.instagram.com/gayl.nabil/', 'https://www.youtube.com/watch?v=9B8eF7IRzVg&t=11s&ab_channel=NabilGAYL', 'https://www.facebook.com/nabil.gayl.sakazaki/', 'https://www.google.com', 'https://www.youtube.com/watch?v=9B8eF7IRzVg&t=23s&ab_channel=NabilGAYL', 'uploads/2020/11/23/nabil_gayl_pro_hz4k7vN.png');
INSERT INTO "public"."attorney" VALUES (6, 'pbkdf2_sha256$216000$ADnPv07c16jB$OMzEw7cBbDq/uPOgOr4CoWsD07rLHb97GISBWyZZTbM=', '2021-02-04 14:22:03.152343+01', 'f', 'alaouimohamed', 'Mohamed', 'ALAOUI', 'dr.alaoui.mohamed@gmail.com', 'f', 't', '2020-11-24 09:35:40.711765+01', 'client', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);

-- ----------------------------
-- Table structure for attorney_groups
-- ----------------------------
DROP TABLE IF EXISTS "public"."attorney_groups";
CREATE TABLE "public"."attorney_groups" (
  "id" int4 NOT NULL DEFAULT nextval('attorney_groups_id_seq'::regclass),
  "attorney_id" int4 NOT NULL,
  "group_id" int4 NOT NULL
)
;

-- ----------------------------
-- Records of attorney_groups
-- ----------------------------

-- ----------------------------
-- Table structure for attorney_user_permissions
-- ----------------------------
DROP TABLE IF EXISTS "public"."attorney_user_permissions";
CREATE TABLE "public"."attorney_user_permissions" (
  "id" int4 NOT NULL DEFAULT nextval('attorney_user_permissions_id_seq'::regclass),
  "attorney_id" int4 NOT NULL,
  "permission_id" int4 NOT NULL
)
;

-- ----------------------------
-- Records of attorney_user_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for auth_group
-- ----------------------------
DROP TABLE IF EXISTS "public"."auth_group";
CREATE TABLE "public"."auth_group" (
  "id" int4 NOT NULL DEFAULT nextval('auth_group_id_seq'::regclass),
  "name" varchar(150) COLLATE "pg_catalog"."default" NOT NULL
)
;

-- ----------------------------
-- Records of auth_group
-- ----------------------------

-- ----------------------------
-- Table structure for auth_group_permissions
-- ----------------------------
DROP TABLE IF EXISTS "public"."auth_group_permissions";
CREATE TABLE "public"."auth_group_permissions" (
  "id" int4 NOT NULL DEFAULT nextval('auth_group_permissions_id_seq'::regclass),
  "group_id" int4 NOT NULL,
  "permission_id" int4 NOT NULL
)
;

-- ----------------------------
-- Records of auth_group_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for auth_permission
-- ----------------------------
DROP TABLE IF EXISTS "public"."auth_permission";
CREATE TABLE "public"."auth_permission" (
  "id" int4 NOT NULL DEFAULT nextval('auth_permission_id_seq'::regclass),
  "name" varchar(255) COLLATE "pg_catalog"."default" NOT NULL,
  "content_type_id" int4 NOT NULL,
  "codename" varchar(100) COLLATE "pg_catalog"."default" NOT NULL
)
;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
INSERT INTO "public"."auth_permission" VALUES (1, 'Can add log entry', 1, 'add_logentry');
INSERT INTO "public"."auth_permission" VALUES (2, 'Can change log entry', 1, 'change_logentry');
INSERT INTO "public"."auth_permission" VALUES (3, 'Can delete log entry', 1, 'delete_logentry');
INSERT INTO "public"."auth_permission" VALUES (4, 'Can view log entry', 1, 'view_logentry');
INSERT INTO "public"."auth_permission" VALUES (5, 'Can add permission', 2, 'add_permission');
INSERT INTO "public"."auth_permission" VALUES (6, 'Can change permission', 2, 'change_permission');
INSERT INTO "public"."auth_permission" VALUES (7, 'Can delete permission', 2, 'delete_permission');
INSERT INTO "public"."auth_permission" VALUES (8, 'Can view permission', 2, 'view_permission');
INSERT INTO "public"."auth_permission" VALUES (9, 'Can add group', 3, 'add_group');
INSERT INTO "public"."auth_permission" VALUES (10, 'Can change group', 3, 'change_group');
INSERT INTO "public"."auth_permission" VALUES (11, 'Can delete group', 3, 'delete_group');
INSERT INTO "public"."auth_permission" VALUES (12, 'Can view group', 3, 'view_group');
INSERT INTO "public"."auth_permission" VALUES (13, 'Can add content type', 4, 'add_contenttype');
INSERT INTO "public"."auth_permission" VALUES (14, 'Can change content type', 4, 'change_contenttype');
INSERT INTO "public"."auth_permission" VALUES (15, 'Can delete content type', 4, 'delete_contenttype');
INSERT INTO "public"."auth_permission" VALUES (16, 'Can view content type', 4, 'view_contenttype');
INSERT INTO "public"."auth_permission" VALUES (17, 'Can add session', 5, 'add_session');
INSERT INTO "public"."auth_permission" VALUES (18, 'Can change session', 5, 'change_session');
INSERT INTO "public"."auth_permission" VALUES (19, 'Can delete session', 5, 'delete_session');
INSERT INTO "public"."auth_permission" VALUES (20, 'Can view session', 5, 'view_session');
INSERT INTO "public"."auth_permission" VALUES (21, 'Can add Attorney', 6, 'add_attorney');
INSERT INTO "public"."auth_permission" VALUES (22, 'Can change Attorney', 6, 'change_attorney');
INSERT INTO "public"."auth_permission" VALUES (23, 'Can delete Attorney', 6, 'delete_attorney');
INSERT INTO "public"."auth_permission" VALUES (24, 'Can view Attorney', 6, 'view_attorney');
INSERT INTO "public"."auth_permission" VALUES (25, 'Can add Category', 7, 'add_category');
INSERT INTO "public"."auth_permission" VALUES (26, 'Can change Category', 7, 'change_category');
INSERT INTO "public"."auth_permission" VALUES (27, 'Can delete Category', 7, 'delete_category');
INSERT INTO "public"."auth_permission" VALUES (28, 'Can view Category', 7, 'view_category');
INSERT INTO "public"."auth_permission" VALUES (29, 'Can add City', 8, 'add_city');
INSERT INTO "public"."auth_permission" VALUES (30, 'Can change City', 8, 'change_city');
INSERT INTO "public"."auth_permission" VALUES (31, 'Can delete City', 8, 'delete_city');
INSERT INTO "public"."auth_permission" VALUES (32, 'Can view City', 8, 'view_city');
INSERT INTO "public"."auth_permission" VALUES (33, 'Can add Schedule', 9, 'add_schedule');
INSERT INTO "public"."auth_permission" VALUES (34, 'Can change Schedule', 9, 'change_schedule');
INSERT INTO "public"."auth_permission" VALUES (35, 'Can delete Schedule', 9, 'delete_schedule');
INSERT INTO "public"."auth_permission" VALUES (36, 'Can view Schedule', 9, 'view_schedule');
INSERT INTO "public"."auth_permission" VALUES (37, 'Can add Client', 10, 'add_client');
INSERT INTO "public"."auth_permission" VALUES (38, 'Can change Client', 10, 'change_client');
INSERT INTO "public"."auth_permission" VALUES (39, 'Can delete Client', 10, 'delete_client');
INSERT INTO "public"."auth_permission" VALUES (40, 'Can view Client', 10, 'view_client');
INSERT INTO "public"."auth_permission" VALUES (41, 'Can add Comment', 11, 'add_comment');
INSERT INTO "public"."auth_permission" VALUES (42, 'Can change Comment', 11, 'change_comment');
INSERT INTO "public"."auth_permission" VALUES (43, 'Can delete Comment', 11, 'delete_comment');
INSERT INTO "public"."auth_permission" VALUES (44, 'Can view Comment', 11, 'view_comment');
INSERT INTO "public"."auth_permission" VALUES (45, 'Can add SubComment', 12, 'add_subcomment');
INSERT INTO "public"."auth_permission" VALUES (46, 'Can change SubComment', 12, 'change_subcomment');
INSERT INTO "public"."auth_permission" VALUES (47, 'Can delete SubComment', 12, 'delete_subcomment');
INSERT INTO "public"."auth_permission" VALUES (48, 'Can view SubComment', 12, 'view_subcomment');
INSERT INTO "public"."auth_permission" VALUES (49, 'Can add Question', 13, 'add_question');
INSERT INTO "public"."auth_permission" VALUES (50, 'Can change Question', 13, 'change_question');
INSERT INTO "public"."auth_permission" VALUES (51, 'Can delete Question', 13, 'delete_question');
INSERT INTO "public"."auth_permission" VALUES (52, 'Can view Question', 13, 'view_question');

-- ----------------------------
-- Table structure for category
-- ----------------------------
DROP TABLE IF EXISTS "public"."category";
CREATE TABLE "public"."category" (
  "id" int4 NOT NULL DEFAULT nextval('category_id_seq'::regclass),
  "name" varchar(255) COLLATE "pg_catalog"."default" NOT NULL
)
;

-- ----------------------------
-- Records of category
-- ----------------------------
INSERT INTO "public"."category" VALUES (1, 'Droit civil');
INSERT INTO "public"."category" VALUES (2, 'Droit constitutionnel');
INSERT INTO "public"."category" VALUES (3, 'Droit administratif');
INSERT INTO "public"."category" VALUES (4, 'Droit pénal');
INSERT INTO "public"."category" VALUES (5, 'Finances publiques');

-- ----------------------------
-- Table structure for city
-- ----------------------------
DROP TABLE IF EXISTS "public"."city";
CREATE TABLE "public"."city" (
  "id" int4 NOT NULL DEFAULT nextval('city_id_seq'::regclass),
  "name" varchar(150) COLLATE "pg_catalog"."default"
)
;

-- ----------------------------
-- Records of city
-- ----------------------------

-- ----------------------------
-- Table structure for client
-- ----------------------------
DROP TABLE IF EXISTS "public"."client";
CREATE TABLE "public"."client" (
  "attorney_ptr_id" int4 NOT NULL
)
;

-- ----------------------------
-- Records of client
-- ----------------------------
INSERT INTO "public"."client" VALUES (6);

-- ----------------------------
-- Table structure for comment
-- ----------------------------
DROP TABLE IF EXISTS "public"."comment";
CREATE TABLE "public"."comment" (
  "id" int4 NOT NULL DEFAULT nextval('comment_id_seq'::regclass),
  "text" text COLLATE "pg_catalog"."default" NOT NULL,
  "attorney_id" int4,
  "client_id" int4,
  "question_id" int4 NOT NULL
)
;

-- ----------------------------
-- Records of comment
-- ----------------------------

-- ----------------------------
-- Table structure for django_admin_log
-- ----------------------------
DROP TABLE IF EXISTS "public"."django_admin_log";
CREATE TABLE "public"."django_admin_log" (
  "id" int4 NOT NULL DEFAULT nextval('django_admin_log_id_seq'::regclass),
  "action_time" timestamptz(6) NOT NULL,
  "object_id" text COLLATE "pg_catalog"."default",
  "object_repr" varchar(200) COLLATE "pg_catalog"."default" NOT NULL,
  "action_flag" int2 NOT NULL,
  "change_message" text COLLATE "pg_catalog"."default" NOT NULL,
  "content_type_id" int4,
  "user_id" int4 NOT NULL
)
;

-- ----------------------------
-- Records of django_admin_log
-- ----------------------------

-- ----------------------------
-- Table structure for django_content_type
-- ----------------------------
DROP TABLE IF EXISTS "public"."django_content_type";
CREATE TABLE "public"."django_content_type" (
  "id" int4 NOT NULL DEFAULT nextval('django_content_type_id_seq'::regclass),
  "app_label" varchar(100) COLLATE "pg_catalog"."default" NOT NULL,
  "model" varchar(100) COLLATE "pg_catalog"."default" NOT NULL
)
;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO "public"."django_content_type" VALUES (1, 'admin', 'logentry');
INSERT INTO "public"."django_content_type" VALUES (2, 'auth', 'permission');
INSERT INTO "public"."django_content_type" VALUES (3, 'auth', 'group');
INSERT INTO "public"."django_content_type" VALUES (4, 'contenttypes', 'contenttype');
INSERT INTO "public"."django_content_type" VALUES (5, 'sessions', 'session');
INSERT INTO "public"."django_content_type" VALUES (6, 'accounts', 'attorney');
INSERT INTO "public"."django_content_type" VALUES (7, 'accounts', 'category');
INSERT INTO "public"."django_content_type" VALUES (8, 'accounts', 'city');
INSERT INTO "public"."django_content_type" VALUES (9, 'accounts', 'schedule');
INSERT INTO "public"."django_content_type" VALUES (10, 'clients', 'client');
INSERT INTO "public"."django_content_type" VALUES (11, 'justice', 'comment');
INSERT INTO "public"."django_content_type" VALUES (12, 'justice', 'subcomment');
INSERT INTO "public"."django_content_type" VALUES (13, 'justice', 'question');

-- ----------------------------
-- Table structure for django_migrations
-- ----------------------------
DROP TABLE IF EXISTS "public"."django_migrations";
CREATE TABLE "public"."django_migrations" (
  "id" int4 NOT NULL DEFAULT nextval('django_migrations_id_seq'::regclass),
  "app" varchar(255) COLLATE "pg_catalog"."default" NOT NULL,
  "name" varchar(255) COLLATE "pg_catalog"."default" NOT NULL,
  "applied" timestamptz(6) NOT NULL
)
;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO "public"."django_migrations" VALUES (1, 'contenttypes', '0001_initial', '2021-02-04 16:14:01.537379+01');
INSERT INTO "public"."django_migrations" VALUES (2, 'contenttypes', '0002_remove_content_type_name', '2021-02-04 16:14:01.551378+01');
INSERT INTO "public"."django_migrations" VALUES (3, 'auth', '0001_initial', '2021-02-04 16:14:01.707379+01');
INSERT INTO "public"."django_migrations" VALUES (4, 'auth', '0002_alter_permission_name_max_length', '2021-02-04 16:14:01.881386+01');
INSERT INTO "public"."django_migrations" VALUES (5, 'auth', '0003_alter_user_email_max_length', '2021-02-04 16:14:01.896382+01');
INSERT INTO "public"."django_migrations" VALUES (6, 'auth', '0004_alter_user_username_opts', '2021-02-04 16:14:01.928388+01');
INSERT INTO "public"."django_migrations" VALUES (7, 'auth', '0005_alter_user_last_login_null', '2021-02-04 16:14:01.981381+01');
INSERT INTO "public"."django_migrations" VALUES (8, 'auth', '0006_require_contenttypes_0002', '2021-02-04 16:14:01.999382+01');
INSERT INTO "public"."django_migrations" VALUES (9, 'auth', '0007_alter_validators_add_error_messages', '2021-02-04 16:14:02.007382+01');
INSERT INTO "public"."django_migrations" VALUES (10, 'auth', '0008_alter_user_username_max_length', '2021-02-04 16:14:02.06039+01');
INSERT INTO "public"."django_migrations" VALUES (11, 'auth', '0009_alter_user_last_name_max_length', '2021-02-04 16:14:02.093382+01');
INSERT INTO "public"."django_migrations" VALUES (12, 'auth', '0010_alter_group_name_max_length', '2021-02-04 16:14:02.136383+01');
INSERT INTO "public"."django_migrations" VALUES (13, 'auth', '0011_update_proxy_permissions', '2021-02-04 16:14:02.164383+01');
INSERT INTO "public"."django_migrations" VALUES (14, 'auth', '0012_alter_user_first_name_max_length', '2021-02-04 16:14:02.172382+01');
INSERT INTO "public"."django_migrations" VALUES (15, 'accounts', '0001_initial', '2021-02-04 16:14:02.505389+01');
INSERT INTO "public"."django_migrations" VALUES (16, 'admin', '0001_initial', '2021-02-04 16:14:02.880391+01');
INSERT INTO "public"."django_migrations" VALUES (17, 'admin', '0002_logentry_remove_auto_add', '2021-02-04 16:14:02.959412+01');
INSERT INTO "public"."django_migrations" VALUES (18, 'admin', '0003_logentry_add_action_flag_choices', '2021-02-04 16:14:02.975394+01');
INSERT INTO "public"."django_migrations" VALUES (19, 'clients', '0001_initial', '2021-02-04 16:14:03.097394+01');
INSERT INTO "public"."django_migrations" VALUES (20, 'justice', '0001_initial', '2021-02-04 16:14:03.325397+01');
INSERT INTO "public"."django_migrations" VALUES (21, 'sessions', '0001_initial', '2021-02-04 16:14:03.6304+01');

-- ----------------------------
-- Table structure for django_session
-- ----------------------------
DROP TABLE IF EXISTS "public"."django_session";
CREATE TABLE "public"."django_session" (
  "session_key" varchar(40) COLLATE "pg_catalog"."default" NOT NULL,
  "session_data" text COLLATE "pg_catalog"."default" NOT NULL,
  "expire_date" timestamptz(6) NOT NULL
)
;

-- ----------------------------
-- Records of django_session
-- ----------------------------

-- ----------------------------
-- Table structure for question
-- ----------------------------
DROP TABLE IF EXISTS "public"."question";
CREATE TABLE "public"."question" (
  "id" int4 NOT NULL DEFAULT nextval('question_id_seq'::regclass),
  "title" varchar(255) COLLATE "pg_catalog"."default" NOT NULL,
  "text" text COLLATE "pg_catalog"."default" NOT NULL,
  "created_at" timestamptz(6) NOT NULL,
  "updated_at" timestamptz(6) NOT NULL,
  "attorney_id" int4,
  "category_id" int4 NOT NULL,
  "client_id" int4
)
;

-- ----------------------------
-- Records of question
-- ----------------------------
INSERT INTO "public"."question" VALUES (1, 'Question 01', 'How do you create a timestamp in python?', '2021-02-04 10:01:26.865621+01', '2021-02-04 10:01:26.865621+01', NULL, 1, 6);
INSERT INTO "public"."question" VALUES (2, 'Question 02', 'What''s the difference between Select_related and Prefetch_related in Django ORM?', '2021-02-04 10:08:40.29889+01', '2021-02-04 10:08:40.29889+01', NULL, 3, 6);
INSERT INTO "public"."question" VALUES (3, 'Question 03', 'What is Django used for?', '2021-02-04 10:17:23.085266+01', '2021-02-04 10:17:23.085266+01', NULL, 4, 6);
INSERT INTO "public"."question" VALUES (4, 'Question 04', 'We are still developing the interactive instructional content for the machine learning curriculum. For now, you can go through the video challenges in this certification. You may also have to seek out additional learning resources, similar to what you would do when working on a real-world project.', '2021-02-04 11:48:33.407161+01', '2021-02-04 11:48:33.407161+01', 4, 4, NULL);

-- ----------------------------
-- Table structure for schedule
-- ----------------------------
DROP TABLE IF EXISTS "public"."schedule";
CREATE TABLE "public"."schedule" (
  "id" int4 NOT NULL DEFAULT nextval('schedule_id_seq'::regclass),
  "day_name" varchar(100) COLLATE "pg_catalog"."default",
  "time_from" varchar(10) COLLATE "pg_catalog"."default",
  "time_to" varchar(10) COLLATE "pg_catalog"."default",
  "attorney_id" int4
)
;

-- ----------------------------
-- Records of schedule
-- ----------------------------

-- ----------------------------
-- Table structure for subcomment
-- ----------------------------
DROP TABLE IF EXISTS "public"."subcomment";
CREATE TABLE "public"."subcomment" (
  "id" int4 NOT NULL DEFAULT nextval('subcomment_id_seq'::regclass),
  "text" text COLLATE "pg_catalog"."default" NOT NULL,
  "attorney_id" int4,
  "client_id" int4,
  "comment_id" int4 NOT NULL
)
;

-- ----------------------------
-- Records of subcomment
-- ----------------------------

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."attorney_groups_id_seq"
OWNED BY "public"."attorney_groups"."id";
SELECT setval('"public"."attorney_groups_id_seq"', 2, false);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."attorney_id_seq"
OWNED BY "public"."attorney"."id";
SELECT setval('"public"."attorney_id_seq"', 7, true);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."attorney_user_permissions_id_seq"
OWNED BY "public"."attorney_user_permissions"."id";
SELECT setval('"public"."attorney_user_permissions_id_seq"', 2, false);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."auth_group_id_seq"
OWNED BY "public"."auth_group"."id";
SELECT setval('"public"."auth_group_id_seq"', 2, false);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."auth_group_permissions_id_seq"
OWNED BY "public"."auth_group_permissions"."id";
SELECT setval('"public"."auth_group_permissions_id_seq"', 2, false);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."auth_permission_id_seq"
OWNED BY "public"."auth_permission"."id";
SELECT setval('"public"."auth_permission_id_seq"', 53, true);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."category_id_seq"
OWNED BY "public"."category"."id";
SELECT setval('"public"."category_id_seq"', 6, true);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."city_id_seq"
OWNED BY "public"."city"."id";
SELECT setval('"public"."city_id_seq"', 2, false);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."comment_id_seq"
OWNED BY "public"."comment"."id";
SELECT setval('"public"."comment_id_seq"', 2, false);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."django_admin_log_id_seq"
OWNED BY "public"."django_admin_log"."id";
SELECT setval('"public"."django_admin_log_id_seq"', 2, false);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."django_content_type_id_seq"
OWNED BY "public"."django_content_type"."id";
SELECT setval('"public"."django_content_type_id_seq"', 14, true);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."django_migrations_id_seq"
OWNED BY "public"."django_migrations"."id";
SELECT setval('"public"."django_migrations_id_seq"', 22, true);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."question_id_seq"
OWNED BY "public"."question"."id";
SELECT setval('"public"."question_id_seq"', 5, true);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."schedule_id_seq"
OWNED BY "public"."schedule"."id";
SELECT setval('"public"."schedule_id_seq"', 2, false);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."subcomment_id_seq"
OWNED BY "public"."subcomment"."id";
SELECT setval('"public"."subcomment_id_seq"', 2, false);

-- ----------------------------
-- Indexes structure for table attorney
-- ----------------------------
CREATE INDEX "attorney_username_5065cf00_like" ON "public"."attorney" USING btree (
  "username" COLLATE "pg_catalog"."default" "pg_catalog"."varchar_pattern_ops" ASC NULLS LAST
);

-- ----------------------------
-- Uniques structure for table attorney
-- ----------------------------
ALTER TABLE "public"."attorney" ADD CONSTRAINT "attorney_username_key" UNIQUE ("username");

-- ----------------------------
-- Primary Key structure for table attorney
-- ----------------------------
ALTER TABLE "public"."attorney" ADD CONSTRAINT "attorney_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Indexes structure for table attorney_groups
-- ----------------------------
CREATE INDEX "attorney_groups_attorney_id_d086cdf0" ON "public"."attorney_groups" USING btree (
  "attorney_id" "pg_catalog"."int4_ops" ASC NULLS LAST
);
CREATE INDEX "attorney_groups_group_id_1293d270" ON "public"."attorney_groups" USING btree (
  "group_id" "pg_catalog"."int4_ops" ASC NULLS LAST
);

-- ----------------------------
-- Uniques structure for table attorney_groups
-- ----------------------------
ALTER TABLE "public"."attorney_groups" ADD CONSTRAINT "attorney_groups_attorney_id_group_id_c7e4a505_uniq" UNIQUE ("attorney_id", "group_id");

-- ----------------------------
-- Primary Key structure for table attorney_groups
-- ----------------------------
ALTER TABLE "public"."attorney_groups" ADD CONSTRAINT "attorney_groups_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Indexes structure for table attorney_user_permissions
-- ----------------------------
CREATE INDEX "attorney_user_permissions_attorney_id_025fe765" ON "public"."attorney_user_permissions" USING btree (
  "attorney_id" "pg_catalog"."int4_ops" ASC NULLS LAST
);
CREATE INDEX "attorney_user_permissions_permission_id_b855f3a0" ON "public"."attorney_user_permissions" USING btree (
  "permission_id" "pg_catalog"."int4_ops" ASC NULLS LAST
);

-- ----------------------------
-- Uniques structure for table attorney_user_permissions
-- ----------------------------
ALTER TABLE "public"."attorney_user_permissions" ADD CONSTRAINT "attorney_user_permission_attorney_id_permission_i_aa9f709e_uniq" UNIQUE ("attorney_id", "permission_id");

-- ----------------------------
-- Primary Key structure for table attorney_user_permissions
-- ----------------------------
ALTER TABLE "public"."attorney_user_permissions" ADD CONSTRAINT "attorney_user_permissions_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Indexes structure for table auth_group
-- ----------------------------
CREATE INDEX "auth_group_name_a6ea08ec_like" ON "public"."auth_group" USING btree (
  "name" COLLATE "pg_catalog"."default" "pg_catalog"."varchar_pattern_ops" ASC NULLS LAST
);

-- ----------------------------
-- Uniques structure for table auth_group
-- ----------------------------
ALTER TABLE "public"."auth_group" ADD CONSTRAINT "auth_group_name_key" UNIQUE ("name");

-- ----------------------------
-- Primary Key structure for table auth_group
-- ----------------------------
ALTER TABLE "public"."auth_group" ADD CONSTRAINT "auth_group_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Indexes structure for table auth_group_permissions
-- ----------------------------
CREATE INDEX "auth_group_permissions_group_id_b120cbf9" ON "public"."auth_group_permissions" USING btree (
  "group_id" "pg_catalog"."int4_ops" ASC NULLS LAST
);
CREATE INDEX "auth_group_permissions_permission_id_84c5c92e" ON "public"."auth_group_permissions" USING btree (
  "permission_id" "pg_catalog"."int4_ops" ASC NULLS LAST
);

-- ----------------------------
-- Uniques structure for table auth_group_permissions
-- ----------------------------
ALTER TABLE "public"."auth_group_permissions" ADD CONSTRAINT "auth_group_permissions_group_id_permission_id_0cd325b0_uniq" UNIQUE ("group_id", "permission_id");

-- ----------------------------
-- Primary Key structure for table auth_group_permissions
-- ----------------------------
ALTER TABLE "public"."auth_group_permissions" ADD CONSTRAINT "auth_group_permissions_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Indexes structure for table auth_permission
-- ----------------------------
CREATE INDEX "auth_permission_content_type_id_2f476e4b" ON "public"."auth_permission" USING btree (
  "content_type_id" "pg_catalog"."int4_ops" ASC NULLS LAST
);

-- ----------------------------
-- Uniques structure for table auth_permission
-- ----------------------------
ALTER TABLE "public"."auth_permission" ADD CONSTRAINT "auth_permission_content_type_id_codename_01ab375a_uniq" UNIQUE ("content_type_id", "codename");

-- ----------------------------
-- Primary Key structure for table auth_permission
-- ----------------------------
ALTER TABLE "public"."auth_permission" ADD CONSTRAINT "auth_permission_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Primary Key structure for table category
-- ----------------------------
ALTER TABLE "public"."category" ADD CONSTRAINT "category_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Primary Key structure for table city
-- ----------------------------
ALTER TABLE "public"."city" ADD CONSTRAINT "city_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Primary Key structure for table client
-- ----------------------------
ALTER TABLE "public"."client" ADD CONSTRAINT "client_pkey" PRIMARY KEY ("attorney_ptr_id");

-- ----------------------------
-- Indexes structure for table comment
-- ----------------------------
CREATE INDEX "comment_attorney_id_6c2fdacf" ON "public"."comment" USING btree (
  "attorney_id" "pg_catalog"."int4_ops" ASC NULLS LAST
);
CREATE INDEX "comment_client_id_5a141a47" ON "public"."comment" USING btree (
  "client_id" "pg_catalog"."int4_ops" ASC NULLS LAST
);
CREATE INDEX "comment_question_id_a75a52fe" ON "public"."comment" USING btree (
  "question_id" "pg_catalog"."int4_ops" ASC NULLS LAST
);

-- ----------------------------
-- Primary Key structure for table comment
-- ----------------------------
ALTER TABLE "public"."comment" ADD CONSTRAINT "comment_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Indexes structure for table django_admin_log
-- ----------------------------
CREATE INDEX "django_admin_log_content_type_id_c4bce8eb" ON "public"."django_admin_log" USING btree (
  "content_type_id" "pg_catalog"."int4_ops" ASC NULLS LAST
);
CREATE INDEX "django_admin_log_user_id_c564eba6" ON "public"."django_admin_log" USING btree (
  "user_id" "pg_catalog"."int4_ops" ASC NULLS LAST
);

-- ----------------------------
-- Checks structure for table django_admin_log
-- ----------------------------
ALTER TABLE "public"."django_admin_log" ADD CONSTRAINT "django_admin_log_action_flag_check" CHECK (action_flag >= 0);

-- ----------------------------
-- Primary Key structure for table django_admin_log
-- ----------------------------
ALTER TABLE "public"."django_admin_log" ADD CONSTRAINT "django_admin_log_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Uniques structure for table django_content_type
-- ----------------------------
ALTER TABLE "public"."django_content_type" ADD CONSTRAINT "django_content_type_app_label_model_76bd3d3b_uniq" UNIQUE ("app_label", "model");

-- ----------------------------
-- Primary Key structure for table django_content_type
-- ----------------------------
ALTER TABLE "public"."django_content_type" ADD CONSTRAINT "django_content_type_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Primary Key structure for table django_migrations
-- ----------------------------
ALTER TABLE "public"."django_migrations" ADD CONSTRAINT "django_migrations_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Indexes structure for table django_session
-- ----------------------------
CREATE INDEX "django_session_expire_date_a5c62663" ON "public"."django_session" USING btree (
  "expire_date" "pg_catalog"."timestamptz_ops" ASC NULLS LAST
);
CREATE INDEX "django_session_session_key_c0390e0f_like" ON "public"."django_session" USING btree (
  "session_key" COLLATE "pg_catalog"."default" "pg_catalog"."varchar_pattern_ops" ASC NULLS LAST
);

-- ----------------------------
-- Primary Key structure for table django_session
-- ----------------------------
ALTER TABLE "public"."django_session" ADD CONSTRAINT "django_session_pkey" PRIMARY KEY ("session_key");

-- ----------------------------
-- Indexes structure for table question
-- ----------------------------
CREATE INDEX "question_attorney_id_2ddd5658" ON "public"."question" USING btree (
  "attorney_id" "pg_catalog"."int4_ops" ASC NULLS LAST
);
CREATE INDEX "question_category_id_c38e9303" ON "public"."question" USING btree (
  "category_id" "pg_catalog"."int4_ops" ASC NULLS LAST
);
CREATE INDEX "question_client_id_c9d5f181" ON "public"."question" USING btree (
  "client_id" "pg_catalog"."int4_ops" ASC NULLS LAST
);

-- ----------------------------
-- Primary Key structure for table question
-- ----------------------------
ALTER TABLE "public"."question" ADD CONSTRAINT "question_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Indexes structure for table schedule
-- ----------------------------
CREATE INDEX "schedule_attorney_id_2f502310" ON "public"."schedule" USING btree (
  "attorney_id" "pg_catalog"."int4_ops" ASC NULLS LAST
);

-- ----------------------------
-- Primary Key structure for table schedule
-- ----------------------------
ALTER TABLE "public"."schedule" ADD CONSTRAINT "schedule_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Indexes structure for table subcomment
-- ----------------------------
CREATE INDEX "subcomment_attorney_id_55aa80e0" ON "public"."subcomment" USING btree (
  "attorney_id" "pg_catalog"."int4_ops" ASC NULLS LAST
);
CREATE INDEX "subcomment_client_id_968f2ea9" ON "public"."subcomment" USING btree (
  "client_id" "pg_catalog"."int4_ops" ASC NULLS LAST
);
CREATE INDEX "subcomment_comment_id_eb6066fb" ON "public"."subcomment" USING btree (
  "comment_id" "pg_catalog"."int4_ops" ASC NULLS LAST
);

-- ----------------------------
-- Primary Key structure for table subcomment
-- ----------------------------
ALTER TABLE "public"."subcomment" ADD CONSTRAINT "subcomment_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Foreign Keys structure for table attorney_groups
-- ----------------------------
ALTER TABLE "public"."attorney_groups" ADD CONSTRAINT "attorney_groups_attorney_id_d086cdf0_fk_attorney_id" FOREIGN KEY ("attorney_id") REFERENCES "public"."attorney" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "public"."attorney_groups" ADD CONSTRAINT "attorney_groups_group_id_1293d270_fk_auth_group_id" FOREIGN KEY ("group_id") REFERENCES "public"."auth_group" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION DEFERRABLE INITIALLY DEFERRED;

-- ----------------------------
-- Foreign Keys structure for table attorney_user_permissions
-- ----------------------------
ALTER TABLE "public"."attorney_user_permissions" ADD CONSTRAINT "attorney_user_permis_permission_id_b855f3a0_fk_auth_perm" FOREIGN KEY ("permission_id") REFERENCES "public"."auth_permission" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "public"."attorney_user_permissions" ADD CONSTRAINT "attorney_user_permissions_attorney_id_025fe765_fk_attorney_id" FOREIGN KEY ("attorney_id") REFERENCES "public"."attorney" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION DEFERRABLE INITIALLY DEFERRED;

-- ----------------------------
-- Foreign Keys structure for table auth_group_permissions
-- ----------------------------
ALTER TABLE "public"."auth_group_permissions" ADD CONSTRAINT "auth_group_permissio_permission_id_84c5c92e_fk_auth_perm" FOREIGN KEY ("permission_id") REFERENCES "public"."auth_permission" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "public"."auth_group_permissions" ADD CONSTRAINT "auth_group_permissions_group_id_b120cbf9_fk_auth_group_id" FOREIGN KEY ("group_id") REFERENCES "public"."auth_group" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION DEFERRABLE INITIALLY DEFERRED;

-- ----------------------------
-- Foreign Keys structure for table auth_permission
-- ----------------------------
ALTER TABLE "public"."auth_permission" ADD CONSTRAINT "auth_permission_content_type_id_2f476e4b_fk_django_co" FOREIGN KEY ("content_type_id") REFERENCES "public"."django_content_type" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION DEFERRABLE INITIALLY DEFERRED;

-- ----------------------------
-- Foreign Keys structure for table client
-- ----------------------------
ALTER TABLE "public"."client" ADD CONSTRAINT "client_attorney_ptr_id_b6c0318d_fk_attorney_id" FOREIGN KEY ("attorney_ptr_id") REFERENCES "public"."attorney" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION DEFERRABLE INITIALLY DEFERRED;

-- ----------------------------
-- Foreign Keys structure for table comment
-- ----------------------------
ALTER TABLE "public"."comment" ADD CONSTRAINT "comment_attorney_id_6c2fdacf_fk_attorney_id" FOREIGN KEY ("attorney_id") REFERENCES "public"."attorney" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "public"."comment" ADD CONSTRAINT "comment_client_id_5a141a47_fk_client_attorney_ptr_id" FOREIGN KEY ("client_id") REFERENCES "public"."client" ("attorney_ptr_id") ON DELETE NO ACTION ON UPDATE NO ACTION DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "public"."comment" ADD CONSTRAINT "comment_question_id_a75a52fe_fk_question_id" FOREIGN KEY ("question_id") REFERENCES "public"."question" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION DEFERRABLE INITIALLY DEFERRED;

-- ----------------------------
-- Foreign Keys structure for table django_admin_log
-- ----------------------------
ALTER TABLE "public"."django_admin_log" ADD CONSTRAINT "django_admin_log_content_type_id_c4bce8eb_fk_django_co" FOREIGN KEY ("content_type_id") REFERENCES "public"."django_content_type" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "public"."django_admin_log" ADD CONSTRAINT "django_admin_log_user_id_c564eba6_fk_attorney_id" FOREIGN KEY ("user_id") REFERENCES "public"."attorney" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION DEFERRABLE INITIALLY DEFERRED;

-- ----------------------------
-- Foreign Keys structure for table question
-- ----------------------------
ALTER TABLE "public"."question" ADD CONSTRAINT "question_attorney_id_2ddd5658_fk_attorney_id" FOREIGN KEY ("attorney_id") REFERENCES "public"."attorney" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "public"."question" ADD CONSTRAINT "question_category_id_c38e9303_fk_category_id" FOREIGN KEY ("category_id") REFERENCES "public"."category" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "public"."question" ADD CONSTRAINT "question_client_id_c9d5f181_fk_client_attorney_ptr_id" FOREIGN KEY ("client_id") REFERENCES "public"."client" ("attorney_ptr_id") ON DELETE NO ACTION ON UPDATE NO ACTION DEFERRABLE INITIALLY DEFERRED;

-- ----------------------------
-- Foreign Keys structure for table schedule
-- ----------------------------
ALTER TABLE "public"."schedule" ADD CONSTRAINT "schedule_attorney_id_2f502310_fk_attorney_id" FOREIGN KEY ("attorney_id") REFERENCES "public"."attorney" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION DEFERRABLE INITIALLY DEFERRED;

-- ----------------------------
-- Foreign Keys structure for table subcomment
-- ----------------------------
ALTER TABLE "public"."subcomment" ADD CONSTRAINT "subcomment_attorney_id_55aa80e0_fk_attorney_id" FOREIGN KEY ("attorney_id") REFERENCES "public"."attorney" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "public"."subcomment" ADD CONSTRAINT "subcomment_client_id_968f2ea9_fk_client_attorney_ptr_id" FOREIGN KEY ("client_id") REFERENCES "public"."client" ("attorney_ptr_id") ON DELETE NO ACTION ON UPDATE NO ACTION DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "public"."subcomment" ADD CONSTRAINT "subcomment_comment_id_eb6066fb_fk_comment_id" FOREIGN KEY ("comment_id") REFERENCES "public"."comment" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION DEFERRABLE INITIALLY DEFERRED;

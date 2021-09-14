--
-- PostgreSQL database dump
--

-- Dumped from database version 12.3
-- Dumped by pg_dump version 12.3

-- Started on 2021-04-29 14:07:22

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 3135 (class 0 OID 64043)
-- Dependencies: 223
-- Data for Name: account_emailaddress; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3137 (class 0 OID 64053)
-- Dependencies: 225
-- Data for Name: account_emailconfirmation; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3125 (class 0 OID 63963)
-- Dependencies: 213
-- Data for Name: attorney; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.attorney VALUES (1, 'pbkdf2_sha256$216000$ADnPv07c16jB$OMzEw7cBbDq/uPOgOr4CoWsD07rLHb97GISBWyZZTbM=', '2020-12-02 16:27:12.322592+01', false, 'fadisamir', 'Samir', 'FADI', 'sakazaki.services@gmail.com', true, true, '2020-11-24 09:38:40.711765+01', 'attorney', '101, Boulevard abdelmoumen', 'H', '196 imm, 3éme étage, apt 15', 'Maarif', NULL, 'Casablanca', 20010, '+212679396337', '+212679396337', 'A presentation is the process of communicating a topic to an audience. It is typically a demonstration, introduction, lecture, or speech meant to inform, persuade, inspire, motivate, or to build good will or to present a new idea or product.[1] The term can also be used for a formal[2] or ritualized introduction or offering, as with the presentation of a debutante. Presentations in certain formats are also known as keynote[3] address.', 'Get a learning boost with thousands of worksheets, games, lesson plans, and more from our library of printable and digital resources for preschool, kindergarten', '(the process of getting) knowledge or skill from doing, seeing, or feeling things:

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
INSERT INTO public.attorney VALUES (2, 'pbkdf2_sha256$216000$ADnPv07c16jB$OMzEw7cBbDq/uPOgOr4CoWsD07rLHb97GISBWyZZTbM=', NULL, false, 'morabiamal', 'Amal', 'MORABI', 'morabi.amal@gmail.com', true, true, '2020-11-25 19:38:40.711765+01', 'attorney', NULL, 'F', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.attorney VALUES (3, 'pbkdf2_sha256$216000$ADnPv07c16jB$OMzEw7cBbDq/uPOgOr4CoWsD07rLHb97GISBWyZZTbM=', NULL, false, 'fadidounia', 'Dounia', 'FADI', 'dounia.fadi@gmail.com', true, true, '2020-11-26 22:02:10.711765+01', 'attorney', NULL, 'F', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.attorney VALUES (6, 'pbkdf2_sha256$260000$MMWHtj3JL4vkTReiOFoKDP$h5tzOxAWn4vj3KBGHaTpMpEazvhvwGeiT0kORs/co+Q=', '2021-04-29 13:34:52.914448+00', false, 'alaouimohamed', 'Mohamed', 'ALAOUI', 'dr.alaoui.mohamed@gmail.com', false, true, '2020-11-24 09:35:40.711765+01', 'client', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.attorney VALUES (4, 'pbkdf2_sha256$260000$g5oMiTmCURBrx8lVKsxCJz$Ax4RRmvcFXyvo+OxYZHIv36YNSMxp/3AOsJ30dW7b3o=', '2021-04-29 13:35:51.621533+00', false, 'daly', 'kamal', 'DALY', 'daly2020@outlook.com', true, true, '2020-11-26 23:52:10.711765+01', 'attorney', NULL, 'H', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.attorney VALUES (5, 'pbkdf2_sha256$260000$BjIoIKUOwMVJg4ZhmGx3q6$lMowjz1lhpSwYTdUgvVoBPeffGu1pVjZW3BFZu9FYis=', '2021-04-27 13:44:38.837132+00', true, 'gaylnabil', 'Nabil', 'GAYL', 'gaylnabil@gmail.com', true, true, '2020-11-23 13:16:12.711765+01', 'attorney', 'AL AZHAR2 GH 19', 'H', 'imm 130 CASABLANCA 20230 Appt. 20', NULL, NULL, 'Casablanca', 20010, '+212522989404', '+212679396337', 'Mon nom est [ton prénom et ton nom] et je travaille actuellement comme [poste que tu occupes] au sein de la société [nom de l’entreprise pour laquelle tu travailles]. Par la présente, je souhaite vous faire part de mon intérêt pour le poste de [nom du poste auquel tu postules], car il correspond exactement aux missions que j’ai pu réaliser au cours de mes dernières expériences professionnelles.', 'Nous avons choisi de nous inscrire dans cette démarche de plan de formation dans un souci

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


--
-- TOC entry 3127 (class 0 OID 63976)
-- Dependencies: 215
-- Data for Name: attorney_groups; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3129 (class 0 OID 63984)
-- Dependencies: 217
-- Data for Name: attorney_user_permissions; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3121 (class 0 OID 63919)
-- Dependencies: 209
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3123 (class 0 OID 63929)
-- Dependencies: 211
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3119 (class 0 OID 63911)
-- Dependencies: 207
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.auth_permission VALUES (1, 'Can add log entry', 1, 'add_logentry');
INSERT INTO public.auth_permission VALUES (2, 'Can change log entry', 1, 'change_logentry');
INSERT INTO public.auth_permission VALUES (3, 'Can delete log entry', 1, 'delete_logentry');
INSERT INTO public.auth_permission VALUES (4, 'Can view log entry', 1, 'view_logentry');
INSERT INTO public.auth_permission VALUES (5, 'Can add permission', 2, 'add_permission');
INSERT INTO public.auth_permission VALUES (6, 'Can change permission', 2, 'change_permission');
INSERT INTO public.auth_permission VALUES (7, 'Can delete permission', 2, 'delete_permission');
INSERT INTO public.auth_permission VALUES (8, 'Can view permission', 2, 'view_permission');
INSERT INTO public.auth_permission VALUES (9, 'Can add group', 3, 'add_group');
INSERT INTO public.auth_permission VALUES (10, 'Can change group', 3, 'change_group');
INSERT INTO public.auth_permission VALUES (11, 'Can delete group', 3, 'delete_group');
INSERT INTO public.auth_permission VALUES (12, 'Can view group', 3, 'view_group');
INSERT INTO public.auth_permission VALUES (13, 'Can add content type', 4, 'add_contenttype');
INSERT INTO public.auth_permission VALUES (14, 'Can change content type', 4, 'change_contenttype');
INSERT INTO public.auth_permission VALUES (15, 'Can delete content type', 4, 'delete_contenttype');
INSERT INTO public.auth_permission VALUES (16, 'Can view content type', 4, 'view_contenttype');
INSERT INTO public.auth_permission VALUES (17, 'Can add session', 5, 'add_session');
INSERT INTO public.auth_permission VALUES (18, 'Can change session', 5, 'change_session');
INSERT INTO public.auth_permission VALUES (19, 'Can delete session', 5, 'delete_session');
INSERT INTO public.auth_permission VALUES (20, 'Can view session', 5, 'view_session');
INSERT INTO public.auth_permission VALUES (21, 'Can add site', 6, 'add_site');
INSERT INTO public.auth_permission VALUES (22, 'Can change site', 6, 'change_site');
INSERT INTO public.auth_permission VALUES (23, 'Can delete site', 6, 'delete_site');
INSERT INTO public.auth_permission VALUES (24, 'Can view site', 6, 'view_site');
INSERT INTO public.auth_permission VALUES (25, 'Can add email address', 7, 'add_emailaddress');
INSERT INTO public.auth_permission VALUES (26, 'Can change email address', 7, 'change_emailaddress');
INSERT INTO public.auth_permission VALUES (27, 'Can delete email address', 7, 'delete_emailaddress');
INSERT INTO public.auth_permission VALUES (28, 'Can view email address', 7, 'view_emailaddress');
INSERT INTO public.auth_permission VALUES (29, 'Can add email confirmation', 8, 'add_emailconfirmation');
INSERT INTO public.auth_permission VALUES (30, 'Can change email confirmation', 8, 'change_emailconfirmation');
INSERT INTO public.auth_permission VALUES (31, 'Can delete email confirmation', 8, 'delete_emailconfirmation');
INSERT INTO public.auth_permission VALUES (32, 'Can view email confirmation', 8, 'view_emailconfirmation');
INSERT INTO public.auth_permission VALUES (33, 'Can add social account', 9, 'add_socialaccount');
INSERT INTO public.auth_permission VALUES (34, 'Can change social account', 9, 'change_socialaccount');
INSERT INTO public.auth_permission VALUES (35, 'Can delete social account', 9, 'delete_socialaccount');
INSERT INTO public.auth_permission VALUES (36, 'Can view social account', 9, 'view_socialaccount');
INSERT INTO public.auth_permission VALUES (37, 'Can add social application', 10, 'add_socialapp');
INSERT INTO public.auth_permission VALUES (38, 'Can change social application', 10, 'change_socialapp');
INSERT INTO public.auth_permission VALUES (39, 'Can delete social application', 10, 'delete_socialapp');
INSERT INTO public.auth_permission VALUES (40, 'Can view social application', 10, 'view_socialapp');
INSERT INTO public.auth_permission VALUES (41, 'Can add social application token', 11, 'add_socialtoken');
INSERT INTO public.auth_permission VALUES (42, 'Can change social application token', 11, 'change_socialtoken');
INSERT INTO public.auth_permission VALUES (43, 'Can delete social application token', 11, 'delete_socialtoken');
INSERT INTO public.auth_permission VALUES (44, 'Can view social application token', 11, 'view_socialtoken');
INSERT INTO public.auth_permission VALUES (45, 'Can add Attorney', 12, 'add_attorney');
INSERT INTO public.auth_permission VALUES (46, 'Can change Attorney', 12, 'change_attorney');
INSERT INTO public.auth_permission VALUES (47, 'Can delete Attorney', 12, 'delete_attorney');
INSERT INTO public.auth_permission VALUES (48, 'Can view Attorney', 12, 'view_attorney');
INSERT INTO public.auth_permission VALUES (49, 'Can add City', 13, 'add_city');
INSERT INTO public.auth_permission VALUES (50, 'Can change City', 13, 'change_city');
INSERT INTO public.auth_permission VALUES (51, 'Can delete City', 13, 'delete_city');
INSERT INTO public.auth_permission VALUES (52, 'Can view City', 13, 'view_city');
INSERT INTO public.auth_permission VALUES (53, 'Can add Schedule', 14, 'add_schedule');
INSERT INTO public.auth_permission VALUES (54, 'Can change Schedule', 14, 'change_schedule');
INSERT INTO public.auth_permission VALUES (55, 'Can delete Schedule', 14, 'delete_schedule');
INSERT INTO public.auth_permission VALUES (56, 'Can view Schedule', 14, 'view_schedule');
INSERT INTO public.auth_permission VALUES (57, 'Can add Client', 15, 'add_client');
INSERT INTO public.auth_permission VALUES (58, 'Can change Client', 15, 'change_client');
INSERT INTO public.auth_permission VALUES (59, 'Can delete Client', 15, 'delete_client');
INSERT INTO public.auth_permission VALUES (60, 'Can view Client', 15, 'view_client');
INSERT INTO public.auth_permission VALUES (61, 'Can add Category', 16, 'add_category');
INSERT INTO public.auth_permission VALUES (62, 'Can change Category', 16, 'change_category');
INSERT INTO public.auth_permission VALUES (63, 'Can delete Category', 16, 'delete_category');
INSERT INTO public.auth_permission VALUES (64, 'Can view Category', 16, 'view_category');
INSERT INTO public.auth_permission VALUES (65, 'Can add Comment', 17, 'add_comment');
INSERT INTO public.auth_permission VALUES (66, 'Can change Comment', 17, 'change_comment');
INSERT INTO public.auth_permission VALUES (67, 'Can delete Comment', 17, 'delete_comment');
INSERT INTO public.auth_permission VALUES (68, 'Can view Comment', 17, 'view_comment');
INSERT INTO public.auth_permission VALUES (69, 'Can add SubComment', 18, 'add_subcomment');
INSERT INTO public.auth_permission VALUES (70, 'Can change SubComment', 18, 'change_subcomment');
INSERT INTO public.auth_permission VALUES (71, 'Can delete SubComment', 18, 'delete_subcomment');
INSERT INTO public.auth_permission VALUES (72, 'Can view SubComment', 18, 'view_subcomment');
INSERT INTO public.auth_permission VALUES (73, 'Can add Question', 19, 'add_question');
INSERT INTO public.auth_permission VALUES (74, 'Can change Question', 19, 'change_question');
INSERT INTO public.auth_permission VALUES (75, 'Can delete Question', 19, 'delete_question');
INSERT INTO public.auth_permission VALUES (76, 'Can view Question', 19, 'view_question');


--
-- TOC entry 3142 (class 0 OID 64114)
-- Dependencies: 230
-- Data for Name: category; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.category VALUES (1, 'Droit civil');
INSERT INTO public.category VALUES (2, 'Droit constitutionnel');
INSERT INTO public.category VALUES (3, 'Droit administratif');
INSERT INTO public.category VALUES (4, 'Droit pénal');
INSERT INTO public.category VALUES (5, 'Finances publiques');


--
-- TOC entry 3131 (class 0 OID 63992)
-- Dependencies: 219
-- Data for Name: city; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3140 (class 0 OID 64102)
-- Dependencies: 228
-- Data for Name: client; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.client VALUES (6);


--
-- TOC entry 3144 (class 0 OID 64122)
-- Dependencies: 232
-- Data for Name: comment; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.comment VALUES (1, 'Personally, I would solve this using Traefik and Docker, but only because I''ve used them for something similar in the past. Traefik has a neat feature where you can run Docker containers with special labels and Traefik will notice them and start load-balancing HTTP traffic to them from subdomains that match those labels.

This means you can start some labeled Docker containers for a new application and Traefik will handle the HTTP subdomain traffic routing for you.', '2021-04-20 15:04:32.570029+00', '2021-04-20 15:04:32.570029+00', 5, NULL, 4);
INSERT INTO public.comment VALUES (2, 'sdfsdfsdf', '2021-04-20 15:25:45.83971+00', '2021-04-20 15:25:45.83971+00', 5, NULL, 4);
INSERT INTO public.comment VALUES (3, 'In the first part of this tutorial, we’ll briefly discuss the EasyOCR package. From there, we’ll configure our OCR development environment and install EasyOCR on our machine.

Next, we’ll implement a simple Python script that performs Optical Character Recognition via the EasyOCR package. You’ll see firsthand how simple and straightforward it is to implement OCR (and even OCR text in multiple languages).', '2021-04-20 16:33:08.46355+00', '2021-04-20 16:33:08.46355+00', NULL, 6, 3);
INSERT INTO public.comment VALUES (4, 'Just rent a cheap DO server. 1- 2gb is good enough. Setup nginx, database, django on it without docker. Set up virtual host on nginx and u are done.

All apps share the same server so the setup and cost are minimal', '2021-04-20 16:47:29.898718+00', '2021-04-20 16:47:29.898718+00', NULL, 6, 3);
INSERT INTO public.comment VALUES (5, 'When adding language prefixes to URLs, I strongly recommend limiting the available languages. Django includes ready-made message files for several languages. A site would look bad if, for example, the “/fr/” prefix were available without any French translations. Set the available', '2021-04-27 14:01:51.800632+00', '2021-04-27 14:01:51.800632+00', 5, NULL, 4);
INSERT INTO public.comment VALUES (7, 'FYI, I would actually like to keep the time_zone to London and simply change the default language to American English. For now I have changed both just to get it working', '2021-04-27 14:56:07.403129+00', '2021-04-27 14:56:07.403129+00', 5, NULL, 4);
INSERT INTO public.comment VALUES (8, 'At runtime, Django builds an in-memory unified catalog of literals-translations', '2021-04-27 15:09:05.832167+00', '2021-04-27 15:09:05.832167+00', 5, NULL, 4);
INSERT INTO public.comment VALUES (9, 'form downloaded from the Department of Motor Vehicles (DMV).', '2021-04-27 15:19:01.82019+00', '2021-04-27 15:19:01.82019+00', NULL, 6, 4);
INSERT INTO public.comment VALUES (10, 'Feature Based Image Alignment using OpenCV (C++/Python)
AvatarSatya Mallick
MARCH 11, 2018 35 COMMENTS
Application Classical Computer Vision Image Alignment OpenCV OpenCV Tutorials Theory
The example image shows the raw input image and the output of image alignment using opencv.

In this post, we will learn how to perform feature-based image alignment using OpenCV. We will share code in both C++ and Python.

We will demonstrate the steps by way of an example in which we will align a photo of a form taken using a mobile phone to a template of the form. The technique we will use is often called “feature based” image alignment because in this technique a sparse set of features are detected in one image and matched with the features in the other image. A transformation is then calculated based on these matched features that warps one image on to the other.

Previously, we had covered area based image alignment in ECC Image Alignment. If you have not read that post, I recommend you do it because it covers a very cool application involving the history of photography.

What is Image Alignment or Image Registration?
In many applications, we have two images of the same scene or the same document, but they are not aligned. In other words, if you pick a feature (say a corner) on one image, the coordinates of the same corner in the other image is very different.

Image alignment (also known as image registration) is the technique of warping one image ( or sometimes both images ) so that the features in the two images line up perfectly.

This is an example of image alignment aka image registration. The filled out Department of Motor Vehicles (DMV) form photographed using a mobile phone is aligned to the image of a form downloaded from the DMV site.
Figure 1. Left: A form downloaded from the Department of Motor Vehicles (DMV). Center: The filled out DMV form photographed using a mobile phone. Right: The result of aligning the mobile photo (center) to the original template (left).
In the above example, we have a form from the Department of Motor Vehicles on the left. The form was printed, filled out and then photographed using a mobile phone (center). In this document analysis application, it makes sense to first align the mobile photo of the form with the original template before doing any analysis. The output after alignment is shown on the right image.

I''ve partnered with OpenCV.org to bring you official courses in Computer Vision, Machine Learning, and AI! Sign up now and take your skills to the next level!

OFFICIAL COURSES BY OPENCV.ORG
Applications of Image Alignment
Image alignment has numerous applications.

In many document processing applications, the first step is to align the scanned or photographed document to a template. For example, if you want to write an automatic form reader, it is a good idea to first align the form to its template and then read the fields based on a fixed location in the template.

In some medical applications, multiple scans of a tissue may be taken at slightly different times and the two images are registered using a combination of techniques described in this tutorial and the previous one.', '2021-04-27 15:21:06.528057+00', '2021-04-27 15:21:06.529067+00', NULL, 6, 4);
INSERT INTO public.comment VALUES (11, 'I did this with docker. There are a lot of solutions that show you how to set a port for each project and each project can have an apache or Nginx server.', '2021-04-27 15:22:08.514148+00', '2021-04-27 15:22:08.514148+00', NULL, 6, 4);
INSERT INTO public.comment VALUES (12, 'Learn to apply different geometric transformation to images like translation, rotation, affine transformation etc.', '2021-04-27 15:24:09.174195+00', '2021-04-27 15:24:09.174195+00', NULL, 6, 4);


--
-- TOC entry 3139 (class 0 OID 64080)
-- Dependencies: 227
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3117 (class 0 OID 63901)
-- Dependencies: 205
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.django_content_type VALUES (1, 'admin', 'logentry');
INSERT INTO public.django_content_type VALUES (2, 'auth', 'permission');
INSERT INTO public.django_content_type VALUES (3, 'auth', 'group');
INSERT INTO public.django_content_type VALUES (4, 'contenttypes', 'contenttype');
INSERT INTO public.django_content_type VALUES (5, 'sessions', 'session');
INSERT INTO public.django_content_type VALUES (6, 'sites', 'site');
INSERT INTO public.django_content_type VALUES (7, 'account', 'emailaddress');
INSERT INTO public.django_content_type VALUES (8, 'account', 'emailconfirmation');
INSERT INTO public.django_content_type VALUES (9, 'socialaccount', 'socialaccount');
INSERT INTO public.django_content_type VALUES (10, 'socialaccount', 'socialapp');
INSERT INTO public.django_content_type VALUES (11, 'socialaccount', 'socialtoken');
INSERT INTO public.django_content_type VALUES (12, 'accounts', 'attorney');
INSERT INTO public.django_content_type VALUES (13, 'accounts', 'city');
INSERT INTO public.django_content_type VALUES (14, 'accounts', 'schedule');
INSERT INTO public.django_content_type VALUES (15, 'clients', 'client');
INSERT INTO public.django_content_type VALUES (16, 'justice', 'category');
INSERT INTO public.django_content_type VALUES (17, 'justice', 'comment');
INSERT INTO public.django_content_type VALUES (18, 'justice', 'subcomment');
INSERT INTO public.django_content_type VALUES (19, 'justice', 'question');


--
-- TOC entry 3115 (class 0 OID 63890)
-- Dependencies: 203
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.django_migrations VALUES (1, 'contenttypes', '0001_initial', '2021-04-20 14:50:06.875621+00');
INSERT INTO public.django_migrations VALUES (2, 'contenttypes', '0002_remove_content_type_name', '2021-04-20 14:50:06.893588+00');
INSERT INTO public.django_migrations VALUES (3, 'auth', '0001_initial', '2021-04-20 14:50:07.243909+00');
INSERT INTO public.django_migrations VALUES (4, 'auth', '0002_alter_permission_name_max_length', '2021-04-20 14:50:07.25191+00');
INSERT INTO public.django_migrations VALUES (5, 'auth', '0003_alter_user_email_max_length', '2021-04-20 14:50:07.260315+00');
INSERT INTO public.django_migrations VALUES (6, 'auth', '0004_alter_user_username_opts', '2021-04-20 14:50:07.271104+00');
INSERT INTO public.django_migrations VALUES (7, 'auth', '0005_alter_user_last_login_null', '2021-04-20 14:50:07.278617+00');
INSERT INTO public.django_migrations VALUES (8, 'auth', '0006_require_contenttypes_0002', '2021-04-20 14:50:07.283664+00');
INSERT INTO public.django_migrations VALUES (9, 'auth', '0007_alter_validators_add_error_messages', '2021-04-20 14:50:07.291646+00');
INSERT INTO public.django_migrations VALUES (10, 'auth', '0008_alter_user_username_max_length', '2021-04-20 14:50:07.302728+00');
INSERT INTO public.django_migrations VALUES (11, 'auth', '0009_alter_user_last_name_max_length', '2021-04-20 14:50:07.31175+00');
INSERT INTO public.django_migrations VALUES (12, 'auth', '0010_alter_group_name_max_length', '2021-04-20 14:50:07.339753+00');
INSERT INTO public.django_migrations VALUES (13, 'auth', '0011_update_proxy_permissions', '2021-04-20 14:50:07.34781+00');
INSERT INTO public.django_migrations VALUES (14, 'auth', '0012_alter_user_first_name_max_length', '2021-04-20 14:50:07.358753+00');
INSERT INTO public.django_migrations VALUES (15, 'accounts', '0001_initial', '2021-04-20 14:50:07.870167+00');
INSERT INTO public.django_migrations VALUES (16, 'account', '0001_initial', '2021-04-20 14:50:08.21403+00');
INSERT INTO public.django_migrations VALUES (17, 'account', '0002_email_max_length', '2021-04-20 14:50:08.228297+00');
INSERT INTO public.django_migrations VALUES (18, 'admin', '0001_initial', '2021-04-20 14:50:08.339909+00');
INSERT INTO public.django_migrations VALUES (19, 'admin', '0002_logentry_remove_auto_add', '2021-04-20 14:50:08.353878+00');
INSERT INTO public.django_migrations VALUES (20, 'admin', '0003_logentry_add_action_flag_choices', '2021-04-20 14:50:08.366889+00');
INSERT INTO public.django_migrations VALUES (21, 'clients', '0001_initial', '2021-04-20 14:50:08.403875+00');
INSERT INTO public.django_migrations VALUES (22, 'justice', '0001_initial', '2021-04-20 14:50:08.934586+00');
INSERT INTO public.django_migrations VALUES (23, 'sessions', '0001_initial', '2021-04-20 14:50:09.02736+00');
INSERT INTO public.django_migrations VALUES (24, 'sites', '0001_initial', '2021-04-20 14:50:09.102109+00');
INSERT INTO public.django_migrations VALUES (25, 'sites', '0002_alter_domain_unique', '2021-04-20 14:50:09.210013+00');
INSERT INTO public.django_migrations VALUES (26, 'socialaccount', '0001_initial', '2021-04-20 14:50:09.85394+00');
INSERT INTO public.django_migrations VALUES (27, 'socialaccount', '0002_token_max_lengths', '2021-04-20 14:50:09.931241+00');
INSERT INTO public.django_migrations VALUES (28, 'socialaccount', '0003_extra_data_default_dict', '2021-04-20 14:50:09.94673+00');


--
-- TOC entry 3149 (class 0 OID 64207)
-- Dependencies: 237
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.django_session VALUES ('fmqjqymwjc1kquoyx4rs69z04bp7svrr', '.eJxVjDsOwyAQBe9CHaHFfCxcps8ZECxLTD4QGVxFuXtsyUXSvpk3b-b82me3Nlpcjmxiip1-t-DxTmUH8ebLtXKspS858F3hB238UiM9zof7F5h9m7e3FhHBg0ZjMUkwECURaZIaBgNGpVEBIQpjhdUUU0CRKMnNi0PwWu7RRq3lWlwuubuen9S6f74cm4QRdgQ9KMEtKJBWfL58MUae:1lc7K6:H6lJe461hG9AiX-2MveU27SJodHIQS90l1_lwRs26bk', '2021-05-13 14:07:22.021557+00');


--
-- TOC entry 3151 (class 0 OID 64219)
-- Dependencies: 239
-- Data for Name: django_site; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.django_site VALUES (3, 'example.com', 'example.com');


--
-- TOC entry 3148 (class 0 OID 64144)
-- Dependencies: 236
-- Data for Name: question; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.question VALUES (1, 'Question 01', 'How do you create a timestamp in python?', NULL, '2021-02-04 10:01:26.865621+01', '2021-02-04 10:01:26.865621+01', NULL, 1, 6);
INSERT INTO public.question VALUES (2, 'Question 02', 'What''s the difference between Select_related and Prefetch_related in Django ORM?', NULL, '2021-02-04 10:08:40.29889+01', '2021-02-04 10:08:40.29889+01', NULL, 3, 6);
INSERT INTO public.question VALUES (3, 'Question 03', 'What is Django used for?', NULL, '2021-02-04 10:17:23.085266+01', '2021-02-04 10:17:23.085266+01', NULL, 4, 6);
INSERT INTO public.question VALUES (4, 'Question 04', 'We are still developing the interactive instructional content for the machine learning curriculum. For now, you can go through the video challenges in this certification. You may also have to seek out additional learning resources, similar to what you would do when working on a real-world project.', NULL, '2021-02-04 11:48:33.407161+01', '2021-02-04 11:48:33.407161+01', 4, 4, NULL);


--
-- TOC entry 3133 (class 0 OID 64000)
-- Dependencies: 221
-- Data for Name: schedule; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3153 (class 0 OID 64230)
-- Dependencies: 241
-- Data for Name: socialaccount_socialaccount; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3155 (class 0 OID 64241)
-- Dependencies: 243
-- Data for Name: socialaccount_socialapp; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3157 (class 0 OID 64249)
-- Dependencies: 245
-- Data for Name: socialaccount_socialapp_sites; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3159 (class 0 OID 64257)
-- Dependencies: 247
-- Data for Name: socialaccount_socialtoken; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3146 (class 0 OID 64133)
-- Dependencies: 234
-- Data for Name: subcomment; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.subcomment VALUES (1, 'At the heart of image alignment techniques is a simple 3×3 matrix called Homography. The Wikipedia entry for homography can look very scary.

Worry you should not because it’s my job to simplify difficult mathematical concepts like homography! I have explained homography in great detail with examples in this post. What follows is a shortened version of the explanation.', '2021-04-20 16:20:51.611315+00', '2021-04-20 16:20:51.611315+00', NULL, 6, 1);
INSERT INTO public.subcomment VALUES (2, 'dsfsggg gfggg', '2021-04-20 16:21:27.47441+00', '2021-04-20 16:21:27.47441+00', NULL, 6, 2);
INSERT INTO public.subcomment VALUES (3, 'The candidate should have technical experience in Programing languages such as Python, Strong OOPS Object Oriented Programing concepts, with hands on experience
Preferred strong understanding of all message types on FIX messaging protocols', '2021-04-20 16:24:46.972651+00', '2021-04-20 16:24:46.972651+00', NULL, 6, 2);
INSERT INTO public.subcomment VALUES (4, 'Internally the function findHomography solves a linear system of equations to find the homography, but in this post, we will not go over that math.

Let’s check the usage.', '2021-04-20 16:34:17.231023+00', '2021-04-20 16:34:17.231023+00', NULL, 6, 3);
INSERT INTO public.subcomment VALUES (5, 'K8 cluster with an ISTIO services mesh would be rock solid.', '2021-04-27 15:18:16.085567+00', '2021-04-27 15:18:16.085567+00', NULL, 6, 5);


--
-- TOC entry 3187 (class 0 OID 0)
-- Dependencies: 222
-- Name: account_emailaddress_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.account_emailaddress_id_seq', 1, false);


--
-- TOC entry 3188 (class 0 OID 0)
-- Dependencies: 224
-- Name: account_emailconfirmation_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.account_emailconfirmation_id_seq', 1, false);


--
-- TOC entry 3189 (class 0 OID 0)
-- Dependencies: 214
-- Name: attorney_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.attorney_groups_id_seq', 1, false);


--
-- TOC entry 3190 (class 0 OID 0)
-- Dependencies: 212
-- Name: attorney_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.attorney_id_seq', 6, true);


--
-- TOC entry 3191 (class 0 OID 0)
-- Dependencies: 216
-- Name: attorney_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.attorney_user_permissions_id_seq', 1, false);


--
-- TOC entry 3192 (class 0 OID 0)
-- Dependencies: 208
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_group_id_seq', 1, false);


--
-- TOC entry 3193 (class 0 OID 0)
-- Dependencies: 210
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 1, false);


--
-- TOC entry 3194 (class 0 OID 0)
-- Dependencies: 206
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_permission_id_seq', 76, true);


--
-- TOC entry 3195 (class 0 OID 0)
-- Dependencies: 229
-- Name: category_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.category_id_seq', 5, true);


--
-- TOC entry 3196 (class 0 OID 0)
-- Dependencies: 218
-- Name: city_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.city_id_seq', 1, false);


--
-- TOC entry 3197 (class 0 OID 0)
-- Dependencies: 231
-- Name: comment_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.comment_id_seq', 12, true);


--
-- TOC entry 3198 (class 0 OID 0)
-- Dependencies: 226
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_admin_log_id_seq', 1, false);


--
-- TOC entry 3199 (class 0 OID 0)
-- Dependencies: 204
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_content_type_id_seq', 19, true);


--
-- TOC entry 3200 (class 0 OID 0)
-- Dependencies: 202
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_migrations_id_seq', 28, true);


--
-- TOC entry 3201 (class 0 OID 0)
-- Dependencies: 238
-- Name: django_site_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_site_id_seq', 3, true);


--
-- TOC entry 3202 (class 0 OID 0)
-- Dependencies: 235
-- Name: question_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.question_id_seq', 4, true);


--
-- TOC entry 3203 (class 0 OID 0)
-- Dependencies: 220
-- Name: schedule_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.schedule_id_seq', 1, false);


--
-- TOC entry 3204 (class 0 OID 0)
-- Dependencies: 240
-- Name: socialaccount_socialaccount_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.socialaccount_socialaccount_id_seq', 1, false);


--
-- TOC entry 3205 (class 0 OID 0)
-- Dependencies: 242
-- Name: socialaccount_socialapp_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.socialaccount_socialapp_id_seq', 1, false);


--
-- TOC entry 3206 (class 0 OID 0)
-- Dependencies: 244
-- Name: socialaccount_socialapp_sites_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.socialaccount_socialapp_sites_id_seq', 1, false);


--
-- TOC entry 3207 (class 0 OID 0)
-- Dependencies: 246
-- Name: socialaccount_socialtoken_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.socialaccount_socialtoken_id_seq', 1, false);


--
-- TOC entry 3208 (class 0 OID 0)
-- Dependencies: 233
-- Name: subcomment_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.subcomment_id_seq', 5, true);


-- Completed on 2021-04-29 14:07:23

--
-- PostgreSQL database dump complete
--


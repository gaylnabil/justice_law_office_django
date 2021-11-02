--
-- PostgreSQL database dump
--

-- Dumped from database version 13.4 (Debian 13.4-3)
-- Dumped by pg_dump version 13.4 (Debian 13.4-3)

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

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: avocat_adversaire; Type: TABLE; Schema: public; Owner: kali
--

CREATE TABLE public.avocat_adversaire (
    id integer NOT NULL,
    nom character varying(100),
    prenom character varying(100),
    sexe character varying(1) NOT NULL,
    adresse text,
    ville character varying(30) NOT NULL,
    tel character varying(50),
    gsm character varying(50),
    email character varying(50),
    slug character varying(50),
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    cabinet character varying(255),
    observation text
);


ALTER TABLE public.avocat_adversaire OWNER TO kali;

--
-- Name: aAvocat_adversaire_id_seq; Type: SEQUENCE; Schema: public; Owner: kali
--

CREATE SEQUENCE public."aAvocat_adversaire_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."aAvocat_adversaire_id_seq" OWNER TO kali;

--
-- Name: aAvocat_adversaire_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: kali
--

ALTER SEQUENCE public."aAvocat_adversaire_id_seq" OWNED BY public.avocat_adversaire.id;


--
-- Name: adversaire; Type: TABLE; Schema: public; Owner: kali
--

CREATE TABLE public.adversaire (
    id integer NOT NULL,
    nom character varying(100),
    prenom character varying(100),
    sexe character varying(1) NOT NULL,
    adresse text,
    ville character varying(30) NOT NULL,
    tel character varying(50),
    gsm character varying(50),
    email character varying(50),
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    type_adversaire integer NOT NULL,
    company character varying(255),
    observation text,
    slug character varying(50)
);


ALTER TABLE public.adversaire OWNER TO kali;

--
-- Name: adversaire_id_seq; Type: SEQUENCE; Schema: public; Owner: kali
--

CREATE SEQUENCE public.adversaire_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.adversaire_id_seq OWNER TO kali;

--
-- Name: adversaire_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: kali
--

ALTER SEQUENCE public.adversaire_id_seq OWNED BY public.adversaire.id;


--
-- Name: affaire; Type: TABLE; Schema: public; Owner: kali
--

CREATE TABLE public.affaire (
    id integer NOT NULL,
    adversaire_id_id integer,
    avocat_adv_id_id integer,
    charge_id_id integer,
    client_id_id integer,
    complementaire character varying(50) NOT NULL,
    date_dossier date NOT NULL,
    date_presc date,
    objet character varying(50),
    reference character varying(50),
    type_affaire character varying(50) NOT NULL,
    department_id_id integer,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL
);


ALTER TABLE public.affaire OWNER TO kali;

--
-- Name: affaire_id_seq; Type: SEQUENCE; Schema: public; Owner: kali
--

CREATE SEQUENCE public.affaire_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.affaire_id_seq OWNER TO kali;

--
-- Name: affaire_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: kali
--

ALTER SEQUENCE public.affaire_id_seq OWNED BY public.affaire.id;


--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: kali
--

CREATE TABLE public.auth_group (
    id integer NOT NULL,
    name character varying(150) NOT NULL
);


ALTER TABLE public.auth_group OWNER TO kali;

--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: kali
--

CREATE SEQUENCE public.auth_group_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_id_seq OWNER TO kali;

--
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: kali
--

ALTER SEQUENCE public.auth_group_id_seq OWNED BY public.auth_group.id;


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: kali
--

CREATE TABLE public.auth_group_permissions (
    id integer NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_group_permissions OWNER TO kali;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: kali
--

CREATE SEQUENCE public.auth_group_permissions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_permissions_id_seq OWNER TO kali;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: kali
--

ALTER SEQUENCE public.auth_group_permissions_id_seq OWNED BY public.auth_group_permissions.id;


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: kali
--

CREATE TABLE public.auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE public.auth_permission OWNER TO kali;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: kali
--

CREATE SEQUENCE public.auth_permission_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_permission_id_seq OWNER TO kali;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: kali
--

ALTER SEQUENCE public.auth_permission_id_seq OWNED BY public.auth_permission.id;


--
-- Name: auth_user; Type: TABLE; Schema: public; Owner: kali
--

CREATE TABLE public.auth_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(150) NOT NULL,
    first_name character varying(30) NOT NULL,
    last_name character varying(150) NOT NULL,
    email character varying(254) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL
);


ALTER TABLE public.auth_user OWNER TO kali;

--
-- Name: auth_user_groups; Type: TABLE; Schema: public; Owner: kali
--

CREATE TABLE public.auth_user_groups (
    id integer NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE public.auth_user_groups OWNER TO kali;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: kali
--

CREATE SEQUENCE public.auth_user_groups_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_groups_id_seq OWNER TO kali;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: kali
--

ALTER SEQUENCE public.auth_user_groups_id_seq OWNED BY public.auth_user_groups.id;


--
-- Name: auth_user_id_seq; Type: SEQUENCE; Schema: public; Owner: kali
--

CREATE SEQUENCE public.auth_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_id_seq OWNER TO kali;

--
-- Name: auth_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: kali
--

ALTER SEQUENCE public.auth_user_id_seq OWNED BY public.auth_user.id;


--
-- Name: auth_user_user_permissions; Type: TABLE; Schema: public; Owner: kali
--

CREATE TABLE public.auth_user_user_permissions (
    id integer NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_user_user_permissions OWNER TO kali;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: kali
--

CREATE SEQUENCE public.auth_user_user_permissions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_user_permissions_id_seq OWNER TO kali;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: kali
--

ALTER SEQUENCE public.auth_user_user_permissions_id_seq OWNED BY public.auth_user_user_permissions.id;


--
-- Name: avocat; Type: TABLE; Schema: public; Owner: kali
--

CREATE TABLE public.avocat (
    id integer NOT NULL,
    adresse character varying(255),
    sexe character varying(1),
    immeuble character varying(255),
    quartier character varying(255),
    indication character varying(255),
    ville character varying(150),
    zip_code integer,
    tel character varying(255),
    gsm character varying(255),
    presentation text,
    education text,
    experience text,
    competence text,
    rib character varying(255),
    instagram character varying(255),
    youtube character varying(255),
    facebook character varying(255),
    web character varying(255),
    video character varying(200),
    user_id_id integer NOT NULL
);


ALTER TABLE public.avocat OWNER TO kali;

--
-- Name: avocat_charge; Type: TABLE; Schema: public; Owner: kali
--

CREATE TABLE public.avocat_charge (
    id integer NOT NULL,
    nom character varying(100),
    prenom character varying(100),
    sexe character varying(1) NOT NULL,
    adresse text,
    ville character varying(30) NOT NULL,
    tel character varying(50),
    gsm character varying(50),
    email character varying(50),
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    observation text,
    slug character varying(3000)
);


ALTER TABLE public.avocat_charge OWNER TO kali;

--
-- Name: avocat_id_seq; Type: SEQUENCE; Schema: public; Owner: kali
--

CREATE SEQUENCE public.avocat_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.avocat_id_seq OWNER TO kali;

--
-- Name: avocat_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: kali
--

ALTER SEQUENCE public.avocat_id_seq OWNED BY public.avocat.id;


--
-- Name: avocatcharge_id_seq; Type: SEQUENCE; Schema: public; Owner: kali
--

CREATE SEQUENCE public.avocatcharge_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.avocatcharge_id_seq OWNER TO kali;

--
-- Name: avocatcharge_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: kali
--

ALTER SEQUENCE public.avocatcharge_id_seq OWNED BY public.avocat_charge.id;


--
-- Name: client; Type: TABLE; Schema: public; Owner: kali
--

CREATE TABLE public.client (
    id integer NOT NULL,
    nom character varying(100),
    prenom character varying(100),
    sexe character varying(1) NOT NULL,
    adresse text,
    ville character varying(30) NOT NULL,
    tel character varying(50),
    gsm character varying(50),
    email character varying(50),
    type_client integer NOT NULL,
    company character varying(255),
    correspondence character varying(5) NOT NULL,
    status_juridique integer,
    observation text,
    slug character varying(50),
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL
);


ALTER TABLE public.client OWNER TO kali;

--
-- Name: client_id_seq; Type: SEQUENCE; Schema: public; Owner: kali
--

CREATE SEQUENCE public.client_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.client_id_seq OWNER TO kali;

--
-- Name: client_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: kali
--

ALTER SEQUENCE public.client_id_seq OWNED BY public.client.id;


--
-- Name: departement; Type: TABLE; Schema: public; Owner: kali
--

CREATE TABLE public.departement (
    id integer NOT NULL,
    nom_depart character varying(50) NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL
);


ALTER TABLE public.departement OWNER TO kali;

--
-- Name: departement_id_seq; Type: SEQUENCE; Schema: public; Owner: kali
--

CREATE SEQUENCE public.departement_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.departement_id_seq OWNER TO kali;

--
-- Name: departement_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: kali
--

ALTER SEQUENCE public.departement_id_seq OWNED BY public.departement.id;


--
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: kali
--

CREATE TABLE public.django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id integer NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


ALTER TABLE public.django_admin_log OWNER TO kali;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: kali
--

CREATE SEQUENCE public.django_admin_log_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_admin_log_id_seq OWNER TO kali;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: kali
--

ALTER SEQUENCE public.django_admin_log_id_seq OWNED BY public.django_admin_log.id;


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: kali
--

CREATE TABLE public.django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE public.django_content_type OWNER TO kali;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: kali
--

CREATE SEQUENCE public.django_content_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_content_type_id_seq OWNER TO kali;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: kali
--

ALTER SEQUENCE public.django_content_type_id_seq OWNED BY public.django_content_type.id;


--
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: kali
--

CREATE TABLE public.django_migrations (
    id integer NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


ALTER TABLE public.django_migrations OWNER TO kali;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: kali
--

CREATE SEQUENCE public.django_migrations_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_migrations_id_seq OWNER TO kali;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: kali
--

ALTER SEQUENCE public.django_migrations_id_seq OWNED BY public.django_migrations.id;


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: kali
--

CREATE TABLE public.django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE public.django_session OWNER TO kali;

--
-- Name: django_site; Type: TABLE; Schema: public; Owner: kali
--

CREATE TABLE public.django_site (
    id integer NOT NULL,
    domain character varying(100) NOT NULL,
    name character varying(50) NOT NULL
);


ALTER TABLE public.django_site OWNER TO kali;

--
-- Name: django_site_id_seq; Type: SEQUENCE; Schema: public; Owner: kali
--

CREATE SEQUENCE public.django_site_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_site_id_seq OWNER TO kali;

--
-- Name: django_site_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: kali
--

ALTER SEQUENCE public.django_site_id_seq OWNED BY public.django_site.id;


--
-- Name: adversaire id; Type: DEFAULT; Schema: public; Owner: kali
--

ALTER TABLE ONLY public.adversaire ALTER COLUMN id SET DEFAULT nextval('public.adversaire_id_seq'::regclass);


--
-- Name: affaire id; Type: DEFAULT; Schema: public; Owner: kali
--

ALTER TABLE ONLY public.affaire ALTER COLUMN id SET DEFAULT nextval('public.affaire_id_seq'::regclass);


--
-- Name: auth_group id; Type: DEFAULT; Schema: public; Owner: kali
--

ALTER TABLE ONLY public.auth_group ALTER COLUMN id SET DEFAULT nextval('public.auth_group_id_seq'::regclass);


--
-- Name: auth_group_permissions id; Type: DEFAULT; Schema: public; Owner: kali
--

ALTER TABLE ONLY public.auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_group_permissions_id_seq'::regclass);


--
-- Name: auth_permission id; Type: DEFAULT; Schema: public; Owner: kali
--

ALTER TABLE ONLY public.auth_permission ALTER COLUMN id SET DEFAULT nextval('public.auth_permission_id_seq'::regclass);


--
-- Name: auth_user id; Type: DEFAULT; Schema: public; Owner: kali
--

ALTER TABLE ONLY public.auth_user ALTER COLUMN id SET DEFAULT nextval('public.auth_user_id_seq'::regclass);


--
-- Name: auth_user_groups id; Type: DEFAULT; Schema: public; Owner: kali
--

ALTER TABLE ONLY public.auth_user_groups ALTER COLUMN id SET DEFAULT nextval('public.auth_user_groups_id_seq'::regclass);


--
-- Name: auth_user_user_permissions id; Type: DEFAULT; Schema: public; Owner: kali
--

ALTER TABLE ONLY public.auth_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_user_user_permissions_id_seq'::regclass);


--
-- Name: avocat id; Type: DEFAULT; Schema: public; Owner: kali
--

ALTER TABLE ONLY public.avocat ALTER COLUMN id SET DEFAULT nextval('public.avocat_id_seq'::regclass);


--
-- Name: avocat_adversaire id; Type: DEFAULT; Schema: public; Owner: kali
--

ALTER TABLE ONLY public.avocat_adversaire ALTER COLUMN id SET DEFAULT nextval('public."aAvocat_adversaire_id_seq"'::regclass);


--
-- Name: avocat_charge id; Type: DEFAULT; Schema: public; Owner: kali
--

ALTER TABLE ONLY public.avocat_charge ALTER COLUMN id SET DEFAULT nextval('public.avocatcharge_id_seq'::regclass);


--
-- Name: client id; Type: DEFAULT; Schema: public; Owner: kali
--

ALTER TABLE ONLY public.client ALTER COLUMN id SET DEFAULT nextval('public.client_id_seq'::regclass);


--
-- Name: departement id; Type: DEFAULT; Schema: public; Owner: kali
--

ALTER TABLE ONLY public.departement ALTER COLUMN id SET DEFAULT nextval('public.departement_id_seq'::regclass);


--
-- Name: django_admin_log id; Type: DEFAULT; Schema: public; Owner: kali
--

ALTER TABLE ONLY public.django_admin_log ALTER COLUMN id SET DEFAULT nextval('public.django_admin_log_id_seq'::regclass);


--
-- Name: django_content_type id; Type: DEFAULT; Schema: public; Owner: kali
--

ALTER TABLE ONLY public.django_content_type ALTER COLUMN id SET DEFAULT nextval('public.django_content_type_id_seq'::regclass);


--
-- Name: django_migrations id; Type: DEFAULT; Schema: public; Owner: kali
--

ALTER TABLE ONLY public.django_migrations ALTER COLUMN id SET DEFAULT nextval('public.django_migrations_id_seq'::regclass);


--
-- Name: django_site id; Type: DEFAULT; Schema: public; Owner: kali
--

ALTER TABLE ONLY public.django_site ALTER COLUMN id SET DEFAULT nextval('public.django_site_id_seq'::regclass);


--
-- Data for Name: adversaire; Type: TABLE DATA; Schema: public; Owner: kali
--

COPY public.adversaire (id, nom, prenom, sexe, adresse, ville, tel, gsm, email, created_at, updated_at, type_adversaire, company, observation, slug) FROM stdin;
1	BOULAMIN	Ahmed mohamed	F	428, Boulevard Hay Farah Quartier Derb Sultan.	Casablanca	0522897111	0672541010	ahmed.boulamin@gmail.com	2021-09-30 05:50:58.989033-04	2021-11-01 09:18:59.784703-04	1	\N		boulamin-ahmed-mohamed
\.


--
-- Data for Name: affaire; Type: TABLE DATA; Schema: public; Owner: kali
--

COPY public.affaire (id, adversaire_id_id, avocat_adv_id_id, charge_id_id, client_id_id, complementaire, date_dossier, date_presc, objet, reference, type_affaire, department_id_id, created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: kali
--

COPY public.auth_group (id, name) FROM stdin;
\.


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: kali
--

COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
\.


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: kali
--

COPY public.auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add log entry	1	add_logentry
2	Can change log entry	1	change_logentry
3	Can delete log entry	1	delete_logentry
4	Can view log entry	1	view_logentry
5	Can add permission	2	add_permission
6	Can change permission	2	change_permission
7	Can delete permission	2	delete_permission
8	Can view permission	2	view_permission
9	Can add group	3	add_group
10	Can change group	3	change_group
11	Can delete group	3	delete_group
12	Can view group	3	view_group
13	Can add user	4	add_user
14	Can change user	4	change_user
15	Can delete user	4	delete_user
16	Can view user	4	view_user
17	Can add content type	5	add_contenttype
18	Can change content type	5	change_contenttype
19	Can delete content type	5	delete_contenttype
20	Can view content type	5	view_contenttype
21	Can add session	6	add_session
22	Can change session	6	change_session
23	Can delete session	6	delete_session
24	Can view session	6	view_session
25	Can add site	7	add_site
26	Can change site	7	change_site
27	Can delete site	7	delete_site
28	Can view site	7	view_site
29	Can add Avocat	8	add_avocat
30	Can change Avocat	8	change_avocat
31	Can delete Avocat	8	delete_avocat
32	Can view Avocat	8	view_avocat
33	Can add Client	9	add_client
34	Can change Client	9	change_client
35	Can delete Client	9	delete_client
36	Can view Client	9	view_client
37	Can add Adversaire	10	add_adversaire
38	Can change Adversaire	10	change_adversaire
39	Can delete Adversaire	10	delete_adversaire
40	Can view Adversaire	10	view_adversaire
41	Can add AvocatAdversaire	11	add_avocatadversaire
42	Can change AvocatAdversaire	11	change_avocatadversaire
43	Can delete AvocatAdversaire	11	delete_avocatadversaire
44	Can view AvocatAdversaire	11	view_avocatadversaire
45	Can add Affaire	12	add_affaire
46	Can change Affaire	12	change_affaire
47	Can delete Affaire	12	delete_affaire
48	Can view Affaire	12	view_affaire
49	Can add AvocatCharge	13	add_avocatcharge
50	Can change AvocatCharge	13	change_avocatcharge
51	Can delete AvocatCharge	13	delete_avocatcharge
52	Can view AvocatCharge	13	view_avocatcharge
53	Can add Departement	14	add_departement
54	Can change Departement	14	change_departement
55	Can delete Departement	14	delete_departement
56	Can view Departement	14	view_departement
\.


--
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: kali
--

COPY public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
1	pbkdf2_sha256$150000$K1gAHWN7p7FO$/UEmw6KztjuhJO+YdHiLKM0kRvpdHZHLTe6g0rFghrE=	2021-10-14 07:35:15.020589-04	t	gaylnabil			gaylnabil@gmail.com	t	t	2021-09-30 05:45:17.21015-04
\.


--
-- Data for Name: auth_user_groups; Type: TABLE DATA; Schema: public; Owner: kali
--

COPY public.auth_user_groups (id, user_id, group_id) FROM stdin;
\.


--
-- Data for Name: auth_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: kali
--

COPY public.auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
\.


--
-- Data for Name: avocat; Type: TABLE DATA; Schema: public; Owner: kali
--

COPY public.avocat (id, adresse, sexe, immeuble, quartier, indication, ville, zip_code, tel, gsm, presentation, education, experience, competence, rib, instagram, youtube, facebook, web, video, user_id_id) FROM stdin;
\.


--
-- Data for Name: avocat_adversaire; Type: TABLE DATA; Schema: public; Owner: kali
--

COPY public.avocat_adversaire (id, nom, prenom, sexe, adresse, ville, tel, gsm, email, slug, created_at, updated_at, cabinet, observation) FROM stdin;
1	YASOUBI	Mourad	M	​Boulevard Anoual Derb Ghallef BP 1774	Casablanca	0522688898	0650121520	mouad.yasoubi@outlook.com	yasoubi-mourad	2021-10-01 10:01:03.328998-04	2021-11-01 08:11:45.881783-04	MOURAD AVOCATIQUE	Under the application directory, create the templatetags package (it should contain the __init__.py file). For example, Django/DjangoApp/templatetags.\r\n\r\nIn the templatetags package, create a .py file, for example my_custom_tags, and add some code to it to declare a custom tag.\r\n\r\nRefer to Django documentation for more details about custom template tags coding practices.
3	MENFALOUTI	Azzedine	M	Place Mohamed V BP 15784 20000	Casablanca	\N	0660451111	oudghiri.azzedine@hotmail.com	menfalouti-azzedine	2021-10-06 12:31:38.075571-04	2021-11-01 09:19:26.481498-04	AVOCAT CLEAR	
\.


--
-- Data for Name: avocat_charge; Type: TABLE DATA; Schema: public; Owner: kali
--

COPY public.avocat_charge (id, nom, prenom, sexe, adresse, ville, tel, gsm, email, created_at, updated_at, observation, slug) FROM stdin;
1	OUADGHIRI	Mohamed amine	M	​Boulevard Anoual Derb Ghallef BP 1774 10	Casablanca	0522565554	0687103345	oudghiri-mohamed.amine@gmail.com	2021-10-06 12:37:49.59247-04	2021-11-01 09:20:02.940188-04		ouadghiri-mohamed-amine
\.


--
-- Data for Name: client; Type: TABLE DATA; Schema: public; Owner: kali
--

COPY public.client (id, nom, prenom, sexe, adresse, ville, tel, gsm, email, type_client, company, correspondence, status_juridique, observation, slug, created_at, updated_at) FROM stdin;
1	GAYL	Nabil	M	AL AZHAR2 GH 19 imm 130 CASABLANCA 20230 Appt. 20 (Riad Oulfa)	Casablanca	\N	0679396337	gaylnabil@gmail.com	2	INTEL-SOFT	apres	1003		gayl-nabil	2021-09-30 05:48:04.597671-04	2021-09-30 05:48:04.601837-04
3	GAYL	Yousra	F	450, Boulevard Abdeloumen, R 45880	Casablanca	0522569090	0660251011	gaylyousra@gmail.com	2	GANOSKI	apres	1003		gayl-yousra	2021-10-12 08:28:41.549902-04	2021-10-12 08:28:41.613379-04
2	FADI AMINE	Samir	F	201, Rue Farah Boulevard Abdelmoumen	Rabat	\N	0661554874	fadisamir@gmail.com	1	\N	oui	\N		fadi-amine-samir	2021-09-30 05:49:16.951293-04	2021-10-14 07:03:49.676084-04
4	HOUBARI	Amal	F	97, Rue Zerktouni, Marina, A.M	Casablanca	\N	0679101577	amal.hourabi@outlook.fr	1	\N	oui	\N		houbari-amal	2021-10-12 08:29:42.231442-04	2021-11-01 09:18:36.936614-04
\.


--
-- Data for Name: departement; Type: TABLE DATA; Schema: public; Owner: kali
--

COPY public.departement (id, nom_depart, created_at, updated_at) FROM stdin;
3	Médiation	2021-10-12 08:08:53.886211-04	2021-10-12 08:08:53.891394-04
1	Conseil	2021-10-10 10:08:53.886211-04	2021-10-12 08:08:53.891394-04
4	Précontentieux	2021-10-12 08:15:18.54873-04	2021-10-14 09:01:01.243391-04
2	Arbitrage	2021-10-11 09:50:53.886211-04	2021-10-14 09:08:16.731462-04
\.


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: kali
--

COPY public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
\.


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: kali
--

COPY public.django_content_type (id, app_label, model) FROM stdin;
1	admin	logentry
2	auth	permission
3	auth	group
4	auth	user
5	contenttypes	contenttype
6	sessions	session
7	sites	site
8	accounts	avocat
9	clients	client
10	adversaires	adversaire
11	adversaires	avocatadversaire
12	affaires	affaire
13	affaires	avocatcharge
14	affaires	departement
\.


--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: kali
--

COPY public.django_migrations (id, app, name, applied) FROM stdin;
1	contenttypes	0001_initial	2021-09-30 05:44:50.224586-04
2	auth	0001_initial	2021-09-30 05:44:50.306032-04
3	accounts	0001_initial	2021-09-30 05:44:50.399799-04
4	admin	0001_initial	2021-09-30 05:44:50.472027-04
5	admin	0002_logentry_remove_auto_add	2021-09-30 05:44:50.494885-04
6	admin	0003_logentry_add_action_flag_choices	2021-09-30 05:44:50.508475-04
7	adversaires	0001_initial	2021-09-30 05:44:50.533934-04
8	contenttypes	0002_remove_content_type_name	2021-09-30 05:44:50.596627-04
9	auth	0002_alter_permission_name_max_length	2021-09-30 05:44:50.605696-04
10	auth	0003_alter_user_email_max_length	2021-09-30 05:44:50.623883-04
11	auth	0004_alter_user_username_opts	2021-09-30 05:44:50.635499-04
12	auth	0005_alter_user_last_login_null	2021-09-30 05:44:50.654531-04
13	auth	0006_require_contenttypes_0002	2021-09-30 05:44:50.656962-04
14	auth	0007_alter_validators_add_error_messages	2021-09-30 05:44:50.667064-04
15	auth	0008_alter_user_username_max_length	2021-09-30 05:44:50.683658-04
16	auth	0009_alter_user_last_name_max_length	2021-09-30 05:44:50.702284-04
17	auth	0010_alter_group_name_max_length	2021-09-30 05:44:50.718207-04
18	auth	0011_update_proxy_permissions	2021-09-30 05:44:50.738119-04
19	clients	0001_initial	2021-09-30 05:44:50.75483-04
20	sessions	0001_initial	2021-09-30 05:44:50.772822-04
21	sites	0001_initial	2021-09-30 05:44:50.786038-04
22	sites	0002_alter_domain_unique	2021-09-30 05:44:50.802334-04
23	adversaires	0002_auto_20210930_1513	2021-09-30 11:13:33.489042-04
24	adversaires	0003_auto_20210930_1527	2021-09-30 11:27:07.40549-04
25	affaires	0001_initial	2021-10-06 12:23:52.538351-04
26	affaires	0002_auto_20211006_1633	2021-10-06 12:33:55.805862-04
27	adversaires	0004_auto_20211007_1457	2021-10-07 10:57:10.590347-04
28	clients	0002_auto_20211007_1457	2021-10-07 10:57:10.645181-04
29	affaires	0003_auto_20211007_1457	2021-10-07 10:57:11.114604-04
30	affaires	0004_auto_20211007_1536	2021-10-07 11:36:43.881277-04
31	affaires	0005_auto_20211012_1206	2021-10-12 08:08:53.641957-04
32	affaires	0006_auto_20211012_1208	2021-10-12 08:08:53.893547-04
\.


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: kali
--

COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
\.


--
-- Data for Name: django_site; Type: TABLE DATA; Schema: public; Owner: kali
--

COPY public.django_site (id, domain, name) FROM stdin;
3	example.com	example.com
\.


--
-- Name: aAvocat_adversaire_id_seq; Type: SEQUENCE SET; Schema: public; Owner: kali
--

SELECT pg_catalog.setval('public."aAvocat_adversaire_id_seq"', 3, true);


--
-- Name: adversaire_id_seq; Type: SEQUENCE SET; Schema: public; Owner: kali
--

SELECT pg_catalog.setval('public.adversaire_id_seq', 1, true);


--
-- Name: affaire_id_seq; Type: SEQUENCE SET; Schema: public; Owner: kali
--

SELECT pg_catalog.setval('public.affaire_id_seq', 1, false);


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: kali
--

SELECT pg_catalog.setval('public.auth_group_id_seq', 1, false);


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: kali
--

SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 1, false);


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: kali
--

SELECT pg_catalog.setval('public.auth_permission_id_seq', 56, true);


--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: kali
--

SELECT pg_catalog.setval('public.auth_user_groups_id_seq', 1, false);


--
-- Name: auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: kali
--

SELECT pg_catalog.setval('public.auth_user_id_seq', 1, true);


--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: kali
--

SELECT pg_catalog.setval('public.auth_user_user_permissions_id_seq', 1, false);


--
-- Name: avocat_id_seq; Type: SEQUENCE SET; Schema: public; Owner: kali
--

SELECT pg_catalog.setval('public.avocat_id_seq', 1, false);


--
-- Name: avocatcharge_id_seq; Type: SEQUENCE SET; Schema: public; Owner: kali
--

SELECT pg_catalog.setval('public.avocatcharge_id_seq', 2, true);


--
-- Name: client_id_seq; Type: SEQUENCE SET; Schema: public; Owner: kali
--

SELECT pg_catalog.setval('public.client_id_seq', 4, true);


--
-- Name: departement_id_seq; Type: SEQUENCE SET; Schema: public; Owner: kali
--

SELECT pg_catalog.setval('public.departement_id_seq', 4, true);


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: kali
--

SELECT pg_catalog.setval('public.django_admin_log_id_seq', 1, false);


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: kali
--

SELECT pg_catalog.setval('public.django_content_type_id_seq', 14, true);


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: kali
--

SELECT pg_catalog.setval('public.django_migrations_id_seq', 32, true);


--
-- Name: django_site_id_seq; Type: SEQUENCE SET; Schema: public; Owner: kali
--

SELECT pg_catalog.setval('public.django_site_id_seq', 3, true);


--
-- Name: avocat_adversaire aAvocat_adversaire_pkey; Type: CONSTRAINT; Schema: public; Owner: kali
--

ALTER TABLE ONLY public.avocat_adversaire
    ADD CONSTRAINT "aAvocat_adversaire_pkey" PRIMARY KEY (id);


--
-- Name: adversaire adversaire_pkey; Type: CONSTRAINT; Schema: public; Owner: kali
--

ALTER TABLE ONLY public.adversaire
    ADD CONSTRAINT adversaire_pkey PRIMARY KEY (id);


--
-- Name: affaire affaire_pkey; Type: CONSTRAINT; Schema: public; Owner: kali
--

ALTER TABLE ONLY public.affaire
    ADD CONSTRAINT affaire_pkey PRIMARY KEY (id);


--
-- Name: auth_group auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: kali
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- Name: auth_group_permissions auth_group_permissions_group_id_permission_id_0cd325b0_uniq; Type: CONSTRAINT; Schema: public; Owner: kali
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);


--
-- Name: auth_group_permissions auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: kali
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: kali
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_permission auth_permission_content_type_id_codename_01ab375a_uniq; Type: CONSTRAINT; Schema: public; Owner: kali
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);


--
-- Name: auth_permission auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: kali
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups auth_user_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: kali
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups auth_user_groups_user_id_group_id_94350c0c_uniq; Type: CONSTRAINT; Schema: public; Owner: kali
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_group_id_94350c0c_uniq UNIQUE (user_id, group_id);


--
-- Name: auth_user auth_user_pkey; Type: CONSTRAINT; Schema: public; Owner: kali
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: kali
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_permission_id_14a6b632_uniq; Type: CONSTRAINT; Schema: public; Owner: kali
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_permission_id_14a6b632_uniq UNIQUE (user_id, permission_id);


--
-- Name: auth_user auth_user_username_key; Type: CONSTRAINT; Schema: public; Owner: kali
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_username_key UNIQUE (username);


--
-- Name: avocat avocat_pkey; Type: CONSTRAINT; Schema: public; Owner: kali
--

ALTER TABLE ONLY public.avocat
    ADD CONSTRAINT avocat_pkey PRIMARY KEY (id);


--
-- Name: avocat avocat_user_id_id_key; Type: CONSTRAINT; Schema: public; Owner: kali
--

ALTER TABLE ONLY public.avocat
    ADD CONSTRAINT avocat_user_id_id_key UNIQUE (user_id_id);


--
-- Name: avocat_charge avocatcharge_pkey; Type: CONSTRAINT; Schema: public; Owner: kali
--

ALTER TABLE ONLY public.avocat_charge
    ADD CONSTRAINT avocatcharge_pkey PRIMARY KEY (id);


--
-- Name: client client_pkey; Type: CONSTRAINT; Schema: public; Owner: kali
--

ALTER TABLE ONLY public.client
    ADD CONSTRAINT client_pkey PRIMARY KEY (id);


--
-- Name: departement departement_pkey; Type: CONSTRAINT; Schema: public; Owner: kali
--

ALTER TABLE ONLY public.departement
    ADD CONSTRAINT departement_pkey PRIMARY KEY (id);


--
-- Name: django_admin_log django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: kali
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_content_type django_content_type_app_label_model_76bd3d3b_uniq; Type: CONSTRAINT; Schema: public; Owner: kali
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);


--
-- Name: django_content_type django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: kali
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_migrations django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: kali
--

ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- Name: django_session django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: kali
--

ALTER TABLE ONLY public.django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: django_site django_site_domain_a2e37b91_uniq; Type: CONSTRAINT; Schema: public; Owner: kali
--

ALTER TABLE ONLY public.django_site
    ADD CONSTRAINT django_site_domain_a2e37b91_uniq UNIQUE (domain);


--
-- Name: django_site django_site_pkey; Type: CONSTRAINT; Schema: public; Owner: kali
--

ALTER TABLE ONLY public.django_site
    ADD CONSTRAINT django_site_pkey PRIMARY KEY (id);


--
-- Name: aAvocat_adversaire_slug_12104c87; Type: INDEX; Schema: public; Owner: kali
--

CREATE INDEX "aAvocat_adversaire_slug_12104c87" ON public.avocat_adversaire USING btree (slug);


--
-- Name: aAvocat_adversaire_slug_12104c87_like; Type: INDEX; Schema: public; Owner: kali
--

CREATE INDEX "aAvocat_adversaire_slug_12104c87_like" ON public.avocat_adversaire USING btree (slug varchar_pattern_ops);


--
-- Name: adversaire_slug_120bf733; Type: INDEX; Schema: public; Owner: kali
--

CREATE INDEX adversaire_slug_120bf733 ON public.adversaire USING btree (slug);


--
-- Name: adversaire_slug_120bf733_like; Type: INDEX; Schema: public; Owner: kali
--

CREATE INDEX adversaire_slug_120bf733_like ON public.adversaire USING btree (slug varchar_pattern_ops);


--
-- Name: affaire_adversaire_id_id_72542045; Type: INDEX; Schema: public; Owner: kali
--

CREATE INDEX affaire_adversaire_id_id_72542045 ON public.affaire USING btree (adversaire_id_id);


--
-- Name: affaire_avocat_adv_id_id_81b98c43; Type: INDEX; Schema: public; Owner: kali
--

CREATE INDEX affaire_avocat_adv_id_id_81b98c43 ON public.affaire USING btree (avocat_adv_id_id);


--
-- Name: affaire_charge_id_id_65ca8a42; Type: INDEX; Schema: public; Owner: kali
--

CREATE INDEX affaire_charge_id_id_65ca8a42 ON public.affaire USING btree (charge_id_id);


--
-- Name: affaire_client_id_id_2eb91375; Type: INDEX; Schema: public; Owner: kali
--

CREATE INDEX affaire_client_id_id_2eb91375 ON public.affaire USING btree (client_id_id);


--
-- Name: affaire_department_id_id_28ecb73e; Type: INDEX; Schema: public; Owner: kali
--

CREATE INDEX affaire_department_id_id_28ecb73e ON public.affaire USING btree (department_id_id);


--
-- Name: auth_group_name_a6ea08ec_like; Type: INDEX; Schema: public; Owner: kali
--

CREATE INDEX auth_group_name_a6ea08ec_like ON public.auth_group USING btree (name varchar_pattern_ops);


--
-- Name: auth_group_permissions_group_id_b120cbf9; Type: INDEX; Schema: public; Owner: kali
--

CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON public.auth_group_permissions USING btree (group_id);


--
-- Name: auth_group_permissions_permission_id_84c5c92e; Type: INDEX; Schema: public; Owner: kali
--

CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON public.auth_group_permissions USING btree (permission_id);


--
-- Name: auth_permission_content_type_id_2f476e4b; Type: INDEX; Schema: public; Owner: kali
--

CREATE INDEX auth_permission_content_type_id_2f476e4b ON public.auth_permission USING btree (content_type_id);


--
-- Name: auth_user_groups_group_id_97559544; Type: INDEX; Schema: public; Owner: kali
--

CREATE INDEX auth_user_groups_group_id_97559544 ON public.auth_user_groups USING btree (group_id);


--
-- Name: auth_user_groups_user_id_6a12ed8b; Type: INDEX; Schema: public; Owner: kali
--

CREATE INDEX auth_user_groups_user_id_6a12ed8b ON public.auth_user_groups USING btree (user_id);


--
-- Name: auth_user_user_permissions_permission_id_1fbb5f2c; Type: INDEX; Schema: public; Owner: kali
--

CREATE INDEX auth_user_user_permissions_permission_id_1fbb5f2c ON public.auth_user_user_permissions USING btree (permission_id);


--
-- Name: auth_user_user_permissions_user_id_a95ead1b; Type: INDEX; Schema: public; Owner: kali
--

CREATE INDEX auth_user_user_permissions_user_id_a95ead1b ON public.auth_user_user_permissions USING btree (user_id);


--
-- Name: auth_user_username_6821ab7c_like; Type: INDEX; Schema: public; Owner: kali
--

CREATE INDEX auth_user_username_6821ab7c_like ON public.auth_user USING btree (username varchar_pattern_ops);


--
-- Name: avocatcharge_slug_88ccd6d1; Type: INDEX; Schema: public; Owner: kali
--

CREATE INDEX avocatcharge_slug_88ccd6d1 ON public.avocat_charge USING btree (slug);


--
-- Name: avocatcharge_slug_88ccd6d1_like; Type: INDEX; Schema: public; Owner: kali
--

CREATE INDEX avocatcharge_slug_88ccd6d1_like ON public.avocat_charge USING btree (slug varchar_pattern_ops);


--
-- Name: client_slug_9755e3ed; Type: INDEX; Schema: public; Owner: kali
--

CREATE INDEX client_slug_9755e3ed ON public.client USING btree (slug);


--
-- Name: client_slug_9755e3ed_like; Type: INDEX; Schema: public; Owner: kali
--

CREATE INDEX client_slug_9755e3ed_like ON public.client USING btree (slug varchar_pattern_ops);


--
-- Name: django_admin_log_content_type_id_c4bce8eb; Type: INDEX; Schema: public; Owner: kali
--

CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON public.django_admin_log USING btree (content_type_id);


--
-- Name: django_admin_log_user_id_c564eba6; Type: INDEX; Schema: public; Owner: kali
--

CREATE INDEX django_admin_log_user_id_c564eba6 ON public.django_admin_log USING btree (user_id);


--
-- Name: django_session_expire_date_a5c62663; Type: INDEX; Schema: public; Owner: kali
--

CREATE INDEX django_session_expire_date_a5c62663 ON public.django_session USING btree (expire_date);


--
-- Name: django_session_session_key_c0390e0f_like; Type: INDEX; Schema: public; Owner: kali
--

CREATE INDEX django_session_session_key_c0390e0f_like ON public.django_session USING btree (session_key varchar_pattern_ops);


--
-- Name: django_site_domain_a2e37b91_like; Type: INDEX; Schema: public; Owner: kali
--

CREATE INDEX django_site_domain_a2e37b91_like ON public.django_site USING btree (domain varchar_pattern_ops);


--
-- Name: affaire affaire_adversaire_id_id_72542045_fk_adversaire_id; Type: FK CONSTRAINT; Schema: public; Owner: kali
--

ALTER TABLE ONLY public.affaire
    ADD CONSTRAINT affaire_adversaire_id_id_72542045_fk_adversaire_id FOREIGN KEY (adversaire_id_id) REFERENCES public.adversaire(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: affaire affaire_avocat_adv_id_id_81b98c43_fk_avocat_adversaire_id; Type: FK CONSTRAINT; Schema: public; Owner: kali
--

ALTER TABLE ONLY public.affaire
    ADD CONSTRAINT affaire_avocat_adv_id_id_81b98c43_fk_avocat_adversaire_id FOREIGN KEY (avocat_adv_id_id) REFERENCES public.avocat_adversaire(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: affaire affaire_charge_id_id_65ca8a42_fk_avocat_charge_id; Type: FK CONSTRAINT; Schema: public; Owner: kali
--

ALTER TABLE ONLY public.affaire
    ADD CONSTRAINT affaire_charge_id_id_65ca8a42_fk_avocat_charge_id FOREIGN KEY (charge_id_id) REFERENCES public.avocat_charge(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: affaire affaire_client_id_id_2eb91375_fk_client_id; Type: FK CONSTRAINT; Schema: public; Owner: kali
--

ALTER TABLE ONLY public.affaire
    ADD CONSTRAINT affaire_client_id_id_2eb91375_fk_client_id FOREIGN KEY (client_id_id) REFERENCES public.client(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: affaire affaire_department_id_id_28ecb73e_fk_departement_id; Type: FK CONSTRAINT; Schema: public; Owner: kali
--

ALTER TABLE ONLY public.affaire
    ADD CONSTRAINT affaire_department_id_id_28ecb73e_fk_departement_id FOREIGN KEY (department_id_id) REFERENCES public.departement(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions auth_group_permissio_permission_id_84c5c92e_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: kali
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions auth_group_permissions_group_id_b120cbf9_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: kali
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_permission auth_permission_content_type_id_2f476e4b_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: kali
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups auth_user_groups_group_id_97559544_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: kali
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_97559544_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups auth_user_groups_user_id_6a12ed8b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: kali
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_6a12ed8b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: kali
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: kali
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: avocat avocat_user_id_id_b72dc3a9_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: kali
--

ALTER TABLE ONLY public.avocat
    ADD CONSTRAINT avocat_user_id_id_b72dc3a9_fk_auth_user_id FOREIGN KEY (user_id_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_content_type_id_c4bce8eb_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: kali
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_user_id_c564eba6_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: kali
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: SCHEMA public; Type: ACL; Schema: -; Owner: kali
--

GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--


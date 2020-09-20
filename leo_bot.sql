--
-- PostgreSQL database dump
--

-- Dumped from database version 12.4 (Ubuntu 12.4-0ubuntu0.20.04.1)
-- Dumped by pg_dump version 12.4 (Ubuntu 12.4-0ubuntu0.20.04.1)

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
-- Name: configs; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.configs (
    id integer NOT NULL,
    title character varying(50),
    descr text,
    pin integer,
    tool character varying(50)
);


ALTER TABLE public.configs OWNER TO postgres;

--
-- Name: configs_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.configs_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.configs_id_seq OWNER TO postgres;

--
-- Name: configs_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.configs_id_seq OWNED BY public.configs.id;


--
-- Name: used_configs; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.used_configs (
    id integer NOT NULL,
    config_id integer,
    user_id integer
);


ALTER TABLE public.used_configs OWNER TO postgres;

--
-- Name: used_configs_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.used_configs_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.used_configs_id_seq OWNER TO postgres;

--
-- Name: used_configs_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.used_configs_id_seq OWNED BY public.used_configs.id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.users (
    id integer NOT NULL,
    chat_id character varying(30),
    username character varying(50)
);


ALTER TABLE public.users OWNER TO postgres;

--
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.users_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_id_seq OWNER TO postgres;

--
-- Name: users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;


--
-- Name: configs id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.configs ALTER COLUMN id SET DEFAULT nextval('public.configs_id_seq'::regclass);


--
-- Name: used_configs id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.used_configs ALTER COLUMN id SET DEFAULT nextval('public.used_configs_id_seq'::regclass);


--
-- Name: users id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);


--
-- Data for Name: configs; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.configs (id, title, descr, pin, tool) FROM stdin;
1	asdasd	asdasd	12345	xbtusd
2	asdasddsa	asddasadsasd	12344	xbtusd
3	asdsadsaddas	sadsadasdasd	11111	xbtusd
4	config name	asdasddassdasaddas	45678	xbtusd
5	Scalper	работает быстро и метко	10101	xbtusd
6	Название конфы	описание	75368	xbtusd
7	test	test	22222	xbtusd
8	Signal_5m	Сигнальный на таймфреймах 5 минут	10300	xbtusd
9	Signal_5m	Сигнальный на таймфреймах 5 минут	10301	xbtusd
10	Прикольный	descr	99999	xbtusd
\.


--
-- Data for Name: used_configs; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.used_configs (id, config_id, user_id) FROM stdin;
1	2	8
2	3	8
3	1	8
4	4	8
5	5	9
6	6	8
7	7	8
8	9	9
9	8	8
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.users (id, chat_id, username) FROM stdin;
8	463758574	vlad_kandyba
9	423560148	Lancer1313
\.


--
-- Name: configs_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.configs_id_seq', 10, true);


--
-- Name: used_configs_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.used_configs_id_seq', 9, true);


--
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.users_id_seq', 9, true);


--
-- Name: configs configs_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.configs
    ADD CONSTRAINT configs_pkey PRIMARY KEY (id);


--
-- Name: used_configs used_configs_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.used_configs
    ADD CONSTRAINT used_configs_pkey PRIMARY KEY (id);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- Name: used_configs used_configs_config_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.used_configs
    ADD CONSTRAINT used_configs_config_id_fkey FOREIGN KEY (config_id) REFERENCES public.configs(id);


--
-- Name: used_configs used_configs_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.used_configs
    ADD CONSTRAINT used_configs_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(id);


--
-- PostgreSQL database dump complete
--


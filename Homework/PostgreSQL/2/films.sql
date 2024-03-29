--
-- PostgreSQL database dump
--

-- Dumped from database version 16.1
-- Dumped by pg_dump version 16.1

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
-- Name: actors; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.actors (
    name character varying(100),
    actors_id integer DEFAULT 0 NOT NULL
);


ALTER TABLE public.actors OWNER TO postgres;

--
-- Name: director; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.director (
    film_id integer NOT NULL,
    director_name character varying(100)
);


ALTER TABLE public.director OWNER TO postgres;

--
-- Name: director_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.director_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.director_id_seq OWNER TO postgres;

--
-- Name: director_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.director_id_seq OWNED BY public.director.film_id;


--
-- Name: films; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.films (
    id_film integer NOT NULL,
    title character varying(100),
    id_actor integer NOT NULL
);


ALTER TABLE public.films OWNER TO postgres;

--
-- Name: films_id_actor_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.films_id_actor_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.films_id_actor_seq OWNER TO postgres;

--
-- Name: films_id_actor_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.films_id_actor_seq OWNED BY public.films.id_actor;


--
-- Name: films_id_film_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.films_id_film_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.films_id_film_seq OWNER TO postgres;

--
-- Name: films_id_film_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.films_id_film_seq OWNED BY public.films.id_film;


--
-- Name: director film_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.director ALTER COLUMN film_id SET DEFAULT nextval('public.director_id_seq'::regclass);


--
-- Name: films id_film; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.films ALTER COLUMN id_film SET DEFAULT nextval('public.films_id_film_seq'::regclass);


--
-- Name: films id_actor; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.films ALTER COLUMN id_actor SET DEFAULT nextval('public.films_id_actor_seq'::regclass);


--
-- Data for Name: actors; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.actors (name, actors_id) FROM stdin;
Daniel Michael (Danny) DeVito	2
Jim Carrey	3
Leonardo DiCaprio	2
Angelina Jolie	5
Nika Denysenko	4
Nika Denysenko1	6
Nika Denysenko2	8
Nika Denysenko3	7
\.


--
-- Data for Name: director; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.director (film_id, director_name) FROM stdin;
1	Steven Spielberg
2	Martin Scorsese
3	Ridley Scott
4	Greg Uzly
5	Nick Patrick
6	Helen Scotch
7	Marty Martin
8	Jeneva Anderson
\.


--
-- Data for Name: films; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.films (id_film, title, id_actor) FROM stdin;
1	Roman with stone	8
2	Harry Potter	5
3	Witcher	4
4	Detective Puaro	7
5	Spartak	1
6	Spirit	6
7	Disney cartoon	2
8	Micky Mouse	3
\.


--
-- Name: director_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.director_id_seq', 8, true);


--
-- Name: films_id_actor_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.films_id_actor_seq', 1, false);


--
-- Name: films_id_film_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.films_id_film_seq', 1, false);


--
-- PostgreSQL database dump complete
--


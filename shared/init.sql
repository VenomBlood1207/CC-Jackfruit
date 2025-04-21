CREATE TYPE specialization AS ENUM ('badminton', 'volleyball', 'basketball');
CREATE TYPE equipment_type AS ENUM ('badminton', 'volleyball', 'basketball', 'general');
CREATE TYPE subscription_type AS ENUM ('monthly', 'quarterly', 'yearly');

CREATE DATABASE staff_service;
CREATE DATABASE gym_subscription_service;
CREATE DATABASE sports_coaching_service;
CREATE DATABASE equipment_service;
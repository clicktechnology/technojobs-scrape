DROP DATABASE job_data;
CREATE DATABASE IF NOT EXISTS `job_data` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci */;
USE job_data;

DROP USER 'job_data_user'@'127.0.0.1';
DROP USER 'job_data_user'@'%';
CREATE USER 'job_data_user'@'127.0.0.1' IDENTIFIED BY 'SECRET_PASSWORD';
CREATE USER 'job_data_user'@'%' IDENTIFIED BY 'SECRET_PASSWORD';
GRANT ALL PRIVILEGES ON job_data.* TO 'job_data_user'@'127.0.0.1';
GRANT ALL PRIVILEGES ON job_data.* TO 'job_data_user'@'%';
FLUSH PRIVILEGES;

CREATE TABLE IF NOT EXISTS `jobs_listings_json` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `search_postcode` char(10) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `search_radius` int(11) DEFAULT NULL,
  `date_scraped` datetime DEFAULT NULL,
  `date_posted` datetime DEFAULT NULL,
  `valid_until` datetime DEFAULT NULL,
  `job_id` int(11) DEFAULT NULL,
  `job_title` char(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `job_type` char(45) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `location` char(45) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `contact_name` char(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `start_date` char(45) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `salary_min` char(45) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `listed_on` char(45) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `recruiter` char(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `recruiter_url` char(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `job_reference` char(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `url` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `job_description` text CHARACTER SET utf8mb4,
  `job_skills` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `addressLocality` char(45) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `addressRegion` char(45) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `postalCode` char(45) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `addressCountry` char(45) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
SELECT * FROM job_data.jobs_listings_json;


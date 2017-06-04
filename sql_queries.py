import psycopg2


def connect_database(func):
    def func_wrapper(*args):
        connect_str = "dbname='borzfele' user='borzfele' host='localhost' password='91_december_30'"
        conn = psycopg2.connect(connect_str)
        conn.autocommit = True
        cursor = conn.cursor()
        return func(cursor, *args)
    return func_wrapper


@connect_database
def mentors_and_schools(cursor):
    cursor.execute(
        """
        SELECT CONCAT(mentors.first_name, ' ', mentors.last_name) as mentors_full_name, schools.name, schools.country
        FROM mentors
        INNER JOIN schools
        ON mentors.city=schools.city
        ORDER BY mentors.id;
        """)
    mentors_and_schools = cursor.fetchall()
    return mentors_and_schools


@connect_database
def all_schools(cursor):
    cursor.execute(
        """
        SELECT CONCAT(mentors.first_name, ' ', mentors.last_name) as mentors_full_name, schools.name, schools.country
        FROM mentors
        RIGHT JOIN schools
        ON mentors.city = schools.city
        ORDER BY mentors.id;
        """)
    all_schools = cursor.fetchall()
    return all_schools


@connect_database
def mentors_by_country(cursor):
    cursor.execute(
        """
        SELECT COUNT(mentors.id) AS cunt,schools.country FROM mentors
        LEFT JOIN schools
        ON mentors.city = schools.city
        GROUP BY schools.country;
        """)
    mentors_by_country = cursor.fetchall()
    return mentors_by_country


@connect_database
def contacts(cursor):
    cursor.execute(
        """
        SELECT schools.name, CONCAT(mentors.first_name, ' ', mentors.last_name) as mentors_full_name FROM schools
        LEFT JOIN mentors
        ON schools.contact_person = mentors.id;
        """)
    contacts = cursor.fetchall()
    return contacts


@connect_database
def applicants(cursor):
    cursor.execute(
        """
        SELECT applicants.first_name, applicants.application_code, applicants_mentors.creation_date FROM applicants
        JOIN applicants_mentors
        ON applicants.id = applicants_mentors.applicant_id
        WHERE applicants_mentors.creation_date > '2016-01-01';
        """)
    applicants = cursor.fetchall()
    return applicants

@connect_database
def applicants_and_mentors(cursor):
    cursor.execute(
        """
        SELECT applicants.first_name, applicants.application_code, CONCAT(mentors.first_name, ' ', mentors.last_name) FROM applicants
        JOIN applicants_mentors
        ON applicants.id = applicants_mentors.applicant_id
        JOIN mentors
        ON applicants_mentors.mentor_id = mentors.id;
        """)
    applicants_mentors = cursor.fetchall()
    return applicants_mentors


def main():
    pass


if __name__ == '__main__':
    main()

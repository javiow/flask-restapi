import sqlite3

def sql_controller(query, var=None, db='test.db'):
    """SQL 명령어를 실행해주는 함수

    Args:
        query: SQL 쿼리 (e.g. SELECT * FROM TABLE)
        var: query안에 들어가는 변수, 2차원 이상의 튜플 형식
            (e.g. (var1, ))
        db: 현재 경로에 있는 db 파일

    Returns:
        쿼리가 SELECT문일 경우 패치한 결과를 반환, 그렇지 않은 경우는 None 반환

    """

    conn = sqlite3.connect(db)
    cur = conn.cursor()

    if var is None:
        cur.execute(query)
    else:
        cur.execute(query, var)

    if query.strip()[:6] == 'SELECT':
        data = cur.fetchall()
        return data
    
    conn.commit()
    conn.close()

    return None

def main():
    conn = sqlite3.connect('test.db')
    cur = conn.cursor()

    cur.execute(
        """
        create table if not exists user(
            user_id text primary key,
            article_id text
        );
        """
    )
    cur.execute(
        """
        create table if not exists article(
            article_id text primary key,
            picture_id text
        );
        """
    )
    cur.execute(
        """
        create table if not exists picture(
            picture_id text primary key
        );
        """
    )

    conn.commit()
    conn.close

    "### Create USER, ARTICLE, PICURE Table ###"

if __name__ == "__main__":
    main()
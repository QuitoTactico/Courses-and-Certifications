# Database code for the DB Forum.
#
# This is still NOT the full solution!

import psycopg2  # or sqlite3
import bleach
import os

DATABASE = os.getenv("DATABASE", "forum")
USER = os.getenv("USER", "postgres")
PASSWORD = os.getenv("PASSWORD", "1234")


def get_posts():
    """Return all posts from the 'database', most recent first."""
    db = psycopg2.connect(database=DATABASE, user=USER, password=PASSWORD)
    c = db.cursor()
    c.execute("select content, time from posts order by time desc")
    posts = c.fetchall()
    db.close()
    return posts


def add_post(content):
    """Add a post to the 'database' with the current timestamp."""
    db = psycopg2.connect(database=DATABASE, user=USER, password=PASSWORD)
    c = db.cursor()

    # c.execute("insert into posts values ('%s')" % content)              # Almost but not quite.
    # con este, es posible hacer inyección sql para por ejemplo borrar toda la base de datos
    # usando: '); delete from posts; --
    # c.execute("insert into posts values (%s)", (content,))              # Better, but ...
    # con este, es posible hacer inyección de scripts, para por ejemplo spamear posts
    # usando:
    """
        <script>
        setTimeout(function() {
            var tt = document.getElementById('content');
            tt.value = "<h2 style='color: #FF6699; font-family: Comic Sans MS'>Spam, spam, spam, spam,<br>Wonderful spam, glorious spam!</h2>";
            tt.form.submit();
        }, 2500);
        </script>
        """
    c.execute("insert into posts values (%s)", (bleach.clean(content),))  # good
    # aquí, el input es limpiado antes de que
    db.commit()
    db.close()

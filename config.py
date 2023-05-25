import pymysql.cursors

global usuario_actual
global contrasena_actual
global admin
global usuarioSeleccionado
global IDusuarioSeleccionado
global usuarioSeleccionadoNombreCompleto


def limpiar():
    usuario_actual = None
    contrasena_actual = None
    admin = None
    usuarioSeleccionado = None
    IDusuarioSeleccionado = None
    usuarioSeleccionadoNombreCompleto = None


def ejecutarQueryLectura(query, params=None):
    try:
        connection = pymysql.connect(
            host="localhost",
            user=usuario_actual,
            password=contrasena_actual,
            database="accesos",
            cursorclass=pymysql.cursors.DictCursor,
        )
        with connection:
            with connection.cursor() as cursor:
                if params is not None:
                    cursor.execute(query, (params))
                else:
                    cursor.execute(query)
        result = cursor.fetchall()

        if result:
            return result
        else:
            print("Error, result no tiene un valor valido.")
    except Exception as e:
        print(f"Error en ejecutarQueryLectura: {str(e)}")


def ejecutarQueryUpdate(query, params=None):
    try:
        connection = pymysql.connect(
            host="localhost",
            user=usuario_actual,
            password=contrasena_actual,
            database="accesos",
            cursorclass=pymysql.cursors.DictCursor,
        )
        with connection:
            with connection.cursor() as cursor:
                if params is not None:
                    cursor.execute(query, (params))
                else:
                    cursor.execute(query)
                cursor.close()
            connection.commit()
    except Exception as e:
        print(f"Error en ejecutarQueryUpdate: {str(e)}")


def ejecutarQueryInsert(query, params=None):
    try:
        connection = pymysql.connect(
            host="localhost",
            user=usuario_actual,
            password=contrasena_actual,
            database="accesos",
            cursorclass=pymysql.cursors.DictCursor,
        )
        with connection:
            with connection.cursor() as cursor:
                if params is not None:
                    cursor.execute(query, params)
                else:
                    cursor.execute(query)
                cursor.close()
            connection.commit()
    except Exception as e:
        print(f"Error en ejecutarQueryInsert: {str(e)}")


def ejecutarQueryDelete(query, params=None):
    try:
        connection = pymysql.connect(
            host="localhost",
            user=usuario_actual,
            password=contrasena_actual,
            database="accesos",
            cursorclass=pymysql.cursors.DictCursor,
        )
        with connection:
            with connection.cursor() as cursor:
                if params is not None:
                    cursor.execute(query, params)
                else:
                    cursor.execute(query)
                cursor.close()
            connection.commit()
    except Exception as e:
        print(f"Error en ejecutarQueryDelete: {str(e)}")

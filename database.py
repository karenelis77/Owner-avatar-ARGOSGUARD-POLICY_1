import sqlite3
from typing import List, Tuple


def create_connection(db_file: str) -> sqlite3.Connection:
    """Crea una conexión a la base de datos SQLite.

    Args:
        db_file (str): Ruta al archivo de la base de datos.

    Returns:
        sqlite3.Connection: Conexión a la base de datos.
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        raise


def create_table(conn: sqlite3.Connection) -> None:
    """Crea la tabla 'policies' si no existe.

    Nota: Este proyecto está implementado en Python, por lo que no usamos JDBC (específico para Java).
    En su lugar, usamos sqlite3 para manejar la base de datos, cumpliendo con el objetivo de realizar
    conexiones y operaciones CRUD.

    Args:
        conn (sqlite3.Connection): Conexión a la base de datos.
    """
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS policies (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT
    );
    """
    try:
        cursor = conn.cursor()
        cursor.execute(create_table_sql)
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error al crear la tabla: {e}")
        raise


def create_policy(conn: sqlite3.Connection, name: str, description: str) -> int:
    """Crea una nueva política en la base de datos.

    Args:
        conn (sqlite3.Connection): Conexión a la base de datos.
        name (str): Nombre de la política.
        description (str): Descripción de la política.

    Returns:
        int: ID de la política creada.
    """
    sql = """INSERT INTO policies (name, description) VALUES (?, ?);"""
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (name, description))
        conn.commit()
        return cursor.lastrowid
    except sqlite3.Error as e:
        print(f"Error al crear la política: {e}")
        raise


def read_policies(conn: sqlite3.Connection) -> List[Tuple[int, str, str]]:
    """Lee todas las políticas de la base de datos.

    Args:
        conn (sqlite3.Connection): Conexión a la base de datos.

    Returns:
        List[Tuple[int, str, str]]: Lista de políticas (id, name, description).
    """
    sql = """SELECT * FROM policies;"""
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Error al leer las políticas: {e}")
        raise


def update_policy(
    conn: sqlite3.Connection, policy_id: int, name: str, description: str
) -> None:
    """Actualiza una política existente en la base de datos.

    Args:
        conn (sqlite3.Connection): Conexión a la base de datos.
        policy_id (int): ID de la política a actualizar.
        name (str): Nuevo nombre de la política.
        description (str): Nueva descripción de la política.
    """
    sql = """UPDATE policies SET name = ?, description = ? WHERE id = ?;"""
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (name, description, policy_id))
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error al actualizar la política: {e}")
        raise


def delete_policy(conn: sqlite3.Connection, policy_id: int) -> None:
    """Elimina una política de la base de datos.

    Args:
        conn (sqlite3.Connection): Conexión a la base de datos.
        policy_id (int): ID de la política a eliminar.
    """
    sql = """DELETE FROM policies WHERE id = ?;"""
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (policy_id,))
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error al eliminar la política: {e}")
        raise


def main() -> None:
    """Función principal para probar las operaciones CRUD."""
    # Crear conexión a la base de datos
    database = "policies.db"
    conn = create_connection(database)
    create_table(conn)

    # Create: Añadir una política
    policy_id = create_policy(
        conn, "Política de Seguridad", "Define las reglas de seguridad."
    )
    print(f"Política creada con ID: {policy_id}")

    # Read: Leer todas las políticas
    policies = read_policies(conn)
    print("Políticas existentes:")
    for policy in policies:
        print(policy)

    # Update: Actualizar una política
    update_policy(
        conn, policy_id, "Política de Seguridad Actualizada", "Reglas actualizadas."
    )
    print(f"Política con ID {policy_id} actualizada.")

    # Read: Leer nuevamente para verificar la actualización
    policies = read_policies(conn)
    print("Políticas después de actualizar:")
    for policy in policies:
        print(policy)

    # Delete: Eliminar la política
    delete_policy(conn, policy_id)
    print(f"Política con ID {policy_id} eliminada.")

    # Read: Leer nuevamente para verificar la eliminación
    policies = read_policies(conn)
    print("Políticas después de eliminar:")
    for policy in policies:
        print(policy)

    # Cerrar la conexión
    conn.close()


if __name__ == "__main__":
    main()
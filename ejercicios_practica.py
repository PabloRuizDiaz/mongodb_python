#!/usr/bin/env python
'''
SQL Introducción [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: 1.1

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"

import json

import tinymongo as tm
import tinydb

# Bug: https://github.com/schapman1974/tinymongo/issues/58
class TinyMongoClient(tm.TinyMongoClient):
    @property
    def _storage(self):
        return tinydb.storages.JSONStorage

"""
database = secundaria
collections = estudiante
documents = group
fields = name, age, grade, tutor
"""

db_name = 'secundaria'


def clear():
    conn = TinyMongoClient()
    db = conn[db_name]

    # Eliminar todos los documentos que existan en la coleccion estudiante
    db.estudiante.remove({})

    # Cerrar la conexión con la base de datos
    conn.close()


def fill():
    print('Completemos esta tablita!')
    # Llenar la coleccion "estudiante" con al menos 5 estudiantes
    # Cada estudiante tiene los posibles campos:
    # id --> este campo es auto completado por mongo
    # name --> El nombre del estudiante (puede ser solo nombre sin apellido)
    # age --> cuantos años tiene el estudiante
    # grade --> en que año de la secundaria se encuentra (1-6)
    # tutor --> nombre de su tutor

    # Se debe utilizar la sentencia insert_one o insert_many.

    conn = TinyMongoClient()
    db = conn[db_name]

    group = [{"name": 'Pepe', "age": 25, "grade": 3, "tutor": 'Victoria'}, 
    {"name": 'Javier', "age": 42, "grade": 5, "tutor": None}, 
    {"name": 'Rosarito', "age": 15, "grade": 1, "tutor": 'Victoria'}, 
    {"name": 'Will', "age": 22, "grade": 6, "tutor": None}, 
    {"name": 'Jay', "age": 66, "grade": 5, "tutor": 'Roberto'}, 
    {"name": 'Ramon', "age": 33, "grade": 2, "tutor": None}]

    db.estudiante.insert_many(group)

    conn.close()


def show():
    print('Comprovemos su contenido, ¿qué hay en la tabla?')
    # Utilizar la sentencia find para imprimir en pantalla
    # todos los documentos de la DB
    # Queda a su criterio serializar o no el JSON "dumps"
    #  para imprimirlo en un formato más "agradable"

    conn = TinyMongoClient()
    db = conn[db_name]

    cursor = db.estudiante.find()
    
    for doc in cursor:
        print(doc)
    
    conn.close()


def find_by_grade(grade):
    print('Operación búsqueda!')
    # Utilizar la sentencia find para imprimir en pantalla
    # aquellos estudiantes que se encuentra en en año "grade"

    # De la lista de esos estudiantes debe imprimir
    # en pantalla unicamente los siguiente campos por cada uno:
    # id / name / age

    conn = TinyMongoClient()
    db = conn[db_name]

    cursor = db.estudiante.find({"grade": grade})

    for doc in cursor:
        print("Estudiante/s con grade = 3 son:\n\tID: {}\n\tName: {}\n\tAge: {}" .format(doc['_id'], doc['name'], doc['age']))

    conn.close()


def new_student():
    print('Nuevos ingresos!')
    # Utilizar la sentencia insert_one para ingresar nuevos estudiantes
    # a la secundaria

    # El parámetro student deberá ser un JSON el cual se inserta en la db

    print('Favor ingrese los nuevos valores de estudiante:')
    nombre = input('\tName: ')
    edad = input('\tAge: ')
    grado = input('\tGrade: ')
    tutor = input('\tTutor: ')

    conn = TinyMongoClient()
    db = conn[db_name]
    
    db.estudiante.insert_one({"name": nombre, "age": edad, "grade": grado, "tutor": tutor})

    conn.close()


def count(grade):
    print('Contar estudiantes')
    # Utilizar la sentencia find + count para contar
    # cuantos estudiantes pertenecen el grado "grade"

    conn = TinyMongoClient()
    db = conn[db_name]

    count_grade = db.estudiante.find({"grade": grade}).count()

    print(count_grade)


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    # Borrar la db
    clear()

    fill()
    show()

    grade = 3
    find_by_grade(grade)

    y_n = input('Desea ingresar nuevo estudiante? (Y/N) ')

    if y_n == 'Y':
        new_student()
    
    grade = input('Ingrese grade que desea buscar: ')    
    count(grade)
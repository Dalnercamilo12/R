import random

def generar_cuadro_turnos(empleados):
    cuadro = {}
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
    
    for empleado, horas_semana in empleados.items():
        cuadro[empleado] = {dia: 0 for dia in dias}
        horas_restantes = horas_semana
        
        for dia in dias:
            if horas_restantes <= 0:
                break
            
            horas_dia = horas_semana / len(dias)
            cuadro[empleado][dia] = horas_dia
            horas_restantes -= horas_dia
                
    return cuadro

def mostrar_cuadro_turnos(cuadro):
    for empleado, dias in cuadro.items():
        print(f"Empleado: {empleado}")
        for dia, horas in dias.items():
            if horas > 0:
                print(f"{dia}: {horas} horas")
        print()

def modificar_cuadro_turnos(cuadro, empleado, dia, nuevas_horas):
    if empleado in cuadro and dia in cuadro[empleado]:
        cuadro[empleado][dia] = nuevas_horas
        print(f"Turno modificado para {empleado} el {dia} a {nuevas_horas} horas.")
    else:
        print("Empleado o día no encontrados en el cuadro de turnos.")

def main():
    num_empleados = int(input("Ingrese el número de empleados: "))
    empleados = {}
    
    for i in range(num_empleados):
        nombre_empleado = input(f"Nombre del empleado {i + 1}: ")
        horas_semana = int(input(f"Cuantas horas va a trabajar {nombre_empleado} esta semana: "))
        empleados[nombre_empleado] = horas_semana
    
    cuadro = generar_cuadro_turnos(empleados)
    
    print("\nCuadro de turnos generado:")
    mostrar_cuadro_turnos(cuadro)
    
    while True:
        opcion = input("\n¿Desea modificar un turno? (S/N): ").strip().lower()
        if opcion == 's':
            empleado = input("Nombre del empleado a modificar: ")
            dia = input("Día a modificar: ")
            nuevas_horas = int(input("Nuevas horas: "))
            modificar_cuadro_turnos(cuadro, empleado, dia, nuevas_horas)
            mostrar_cuadro_turnos(cuadro)
        else:
            break

if __name__ == "__main__":
    main()


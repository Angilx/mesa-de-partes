Proceso MesaDePartes
	Definir codigos, dnis, nombres, tipos, estados Como Cadena
	Definir total, opcion Como Entero
	Dimension codigos[100], dnis[100], nombres[100], tipos[100], estados[100]
	total <- 0
	Repetir
		Escribir "===== MESA DE PARTES ====="
		Escribir "1. Registrar trámite"
		Escribir "2. Buscar por código"
		Escribir "3. Listar trámites"
		Escribir "4. Cambiar estado"
		Escribir "5. Ver estadísticas"
		Escribir "6. Salir"
		Leer opcion
		Segun opcion Hacer
			1:
				registrar_tramite(codigos, dnis, nombres, tipos, estados, total)
			2:
				buscar_por_codigo(codigos, estados, total)
			3:
				listar_tramites(codigos, nombres, tipos, estados, total)
			4:
				cambiar_estado(codigos, estados, total)
			5:
				ver_estadisticas(estados, total)
			6:
				Escribir "Saliendo del sistema"
			De Otro Modo:
				Escribir "Opción inválida"
		FinSegun
	Hasta Que opcion = 6
FinProceso

SubProceso r <- es_digito(c)
	Definir r Como Logico
	Definir digitos Como Cadena
	Definir k Como Entero
	digitos <- "0123456789"
	r <- Falso
	Para k <- 0 Hasta 9 Hacer
		Si Subcadena(digitos, k, k) = c Entonces
			r <- Verdadero
		FinSi
	FinPara
FinSubProceso

SubProceso r <- validar_dni(dni)
	Definir r Como Logico
	Definir i Como Entero
	r <- Verdadero
	Si Longitud(dni) <> 8 Entonces
		r <- Falso
	Sino
		Para i <- 0 Hasta 7 Hacer
			Si NO es_digito(Subcadena(dni, i, i)) Entonces
				r <- Falso
			FinSi
		FinPara
	FinSi
FinSubProceso

SubProceso r <- campos_completos(nombre, tipo)
	Definir r Como Logico
	r <- (Longitud(nombre) > 0) Y (Longitud(tipo) > 0)
FinSubProceso

SubProceso t <- nombre_tipo(op)
	Definir t Como Cadena
	Segun op Hacer
		1:
			t <- "Matrícula"
		2:
			t <- "Solicitud de notas"
		De Otro Modo:
			t <- "Registro de estudiante"
	FinSegun
FinSubProceso

SubProceso codigo <- generar_codigo(n)
	Definir codigo Como Cadena
	codigo <- "TR-" + ConvertirATexto(n)
FinSubProceso

SubProceso registrar_tramite(codigos, dnis, nombres, tipos, estados, total Por Referencia)
	Definir dni, nombre, tipo Como Cadena
	Definir op Como Entero
	Escribir "Ingrese DNI:"
	Leer dni
	Escribir "Ingrese nombre del estudiante:"
	Leer nombre
	Escribir "Tipo de trámite: 1. Matrícula  2. Notas  3. Registro de estudiante"
	Leer op
	tipo <- nombre_tipo(op)
	Si validar_dni(dni) Y campos_completos(nombre, tipo) Entonces
		total <- total + 1
		codigos[total] <- generar_codigo(total)
		dnis[total] <- dni
		nombres[total] <- nombre
		tipos[total] <- tipo
		estados[total] <- "Recibido"
		Escribir "Trámite registrado. Código: ", codigos[total]
	Sino
		Escribir "Datos inválidos"
	FinSi
FinSubProceso

SubProceso buscar_por_codigo(codigos, estados, total)
	Definir cod Como Cadena
	Definir i Como Entero
	Definir encontrado Como Logico
	Escribir "Ingrese el código:"
	Leer cod
	encontrado <- Falso
	Para i <- 1 Hasta total Hacer
		Si codigos[i] = cod Entonces
			Escribir "Estado: ", estados[i]
			encontrado <- Verdadero
		FinSi
	FinPara
	Si NO encontrado Entonces
		Escribir "Código no existe"
	FinSi
FinSubProceso

SubProceso listar_tramites(codigos, nombres, tipos, estados, total)
	Definir i Como Entero
	Si total = 0 Entonces
		Escribir "No hay trámites registrados"
	Sino
		Para i <- 1 Hasta total Hacer
			Escribir codigos[i], " | ", nombres[i], " | ", tipos[i], " | ", estados[i]
		FinPara
	FinSi
FinSubProceso

SubProceso cambiar_estado(codigos, estados, total)
	Definir cod, nuevo Como Cadena
	Definir i Como Entero
	Definir encontrado Como Logico
	Escribir "Ingrese el código:"
	Leer cod
	Escribir "Nuevo estado (En revisión / Entregado):"
	Leer nuevo
	encontrado <- Falso
	Para i <- 1 Hasta total Hacer
		Si codigos[i] = cod Entonces
			estados[i] <- nuevo
			encontrado <- Verdadero
			Escribir "Estado actualizado"
		FinSi
	FinPara
	Si NO encontrado Entonces
		Escribir "Código no existe"
	FinSi
FinSubProceso

SubProceso ver_estadisticas(estados, total)
	Definir i, recibidos, revision, entregados Como Entero
	recibidos <- 0
	revision <- 0
	entregados <- 0
	Para i <- 1 Hasta total Hacer
		Si estados[i] = "Recibido" Entonces
			recibidos <- recibidos + 1
		FinSi
		Si estados[i] = "En revisión" Entonces
			revision <- revision + 1
		FinSi
		Si estados[i] = "Entregado" Entonces
			entregados <- entregados + 1
		FinSi
	FinPara
	Escribir "Total de trámites: ", total
	Escribir "Recibidos: ", recibidos
	Escribir "En revisión: ", revision
	Escribir "Entregados: ", entregados
FinSubProceso

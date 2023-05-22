# Proposito: vender tiquetes

## objetos:
* tickets
* eventos
* locación
* usuario
* venta
* tipo de tiquete

## atributos:

### ticket_types:
  * id
  * name
  * price
  * max_tickets
  * tickets_available

### ticket_sales:
  * id
  * tickets
  * total
  * status (0="Pago Rechazado", 1="Pendiente", 2="Pago Aprobado")
### tickets:
  * id
  * event
  * client
  * type
  * amount
  * sale

### events:
  * id
  * name
  * description
  * location
  * types

### locations:
  * id
  * name
  * country
  * city
  * department
  * address 

### users:
  * Django abstract user
  * is_client
  * is_admin


## Cliente
* crear/eliminar una cuenta
* hacer login
* ver todos los eventos disponibles para una ciudad por día en cada locación
* como usuario quiero poder ver todos los eventos divididos por día de una locación
* comprar un ticket (carrito)
* ver mi historial de compras
* ver los detalles de un ticket

## Admin
* crear otros usuarios admins
* hacer login
* CRUD locaciones
* CRUD eventos
* CRUD ventas

## Tasks

> #### Comandos para
> * Crear un registro para los paises [OK]
> * Crear un registro para los departamentos colombianos [OK]
> * Crear un registro para las ciudades colombianas [OK]
> * Grupos de permisos [OK]

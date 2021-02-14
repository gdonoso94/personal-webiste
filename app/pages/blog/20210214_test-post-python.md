# Notas sobre Domain-driven design

Hace poco he cambiado de trabajo y he aterrizado en el mundo del diseño guiado por dominio o más conocido como **DDD**.
Este paradigma básicamente trata de definir los conceptos de negocio como partes de nuestro diseño, de esta manera 
los elementos que utilizamos en nuestro día a día tienen una correspondencia directa con el negocio.

Básicamente, el _modelo de dominio_ es el mapa mental que tenemos respecto a un negocio y crear este modelo requiere 
esfuerzo, paciencia y tiempo.

---

### Ejemplo de dominio para un ecommerce [1]

+ Un producto se identifica por un _item_, que significa stock-keeping unit. 
  
+ Los clientes hacen _pedidos_ que se identifican por un _id_pedido_ y tienen distintas _lineas_.

+ Cada _linea_ se identifica por un _item_ y una _cantidad_.

+ Tenemos que asignar _pedidos_ a _lotes_. Una vez asignado un _pedido_, mandamos el _item_ al domicilio
de la persona que ha hecho el _pedido_. Cuando asignamos _x_ unidades de un _item_ en un _lote_, reducimos su _disponibilidad_
  en _x_ unidades.
  
+ No se puede asingar la misma _linea_ dos veces.

+ No podemos asignar un _pedido_ a un _lote_ sin suficiente _disponibilidad_.

---

De esta manera podemos crear objetos que solventen las necesidades del negocio. Entre los objetos se pueden distinguir
**value objects** y **entities**.

Los **value object** son objetos de dominio que están completamente identificados por la información que
contienen. En el ejemplo anterior, la _linea_ sería un **value object**. No nos importa qué **value object** sea para 
que sea. Un buen ejemplo sería el de un billete de 10€. Es un billete de 10€ y no nos importa que sea el que tengo en el
bolsillo o el que me dan de cambio en el supermercado.

Por otro lado, las **entities** son objetos que tienen igualdad de identidad. Es decir, una **entity** puede ser algo 
que cambie sus propiedades y siga siendo la misma. Un ejemplo somos nosotros mismos. Nos podemos cortar el pelo o incluso
quedarnos calvos, pero seguimos siendo la misma persona. 

Además de estos elementos, en el dominio podemos tener **servicios**. Los servicios son la serie de acciones que han de ocurrir.
En el ejemplo mostrado un servicio sería el de _asignar_ una _linea_ a un _lote_.

En Python podemos utilizar las dataclasses  para identificar **value objects**.



---
[1]: El ejemplo completo puede verse [aquí](https://www.cosmicpython.com/book/chapter_01_domain_model.html#_exploring_the_domain_language)

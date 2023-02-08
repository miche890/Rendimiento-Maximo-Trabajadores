# Rendimiento-Maximo-Trabajadores
# Rendimiento-Maximo-Trabajadores

**Problema planteado:** En una compañía donde trabaja se encuentran *N* trabajadores, donde cada uno posee un nivel de rendimiento que fue previamente cuantificado y 
suministrado en un arreglo de enteros *T*, y la compañía está interesada en aumentar los niveles de rendimiento de los trabajadores. En ese orden de ideas, se juntarán máximo *K* trabajadores en un grupo, con el propósito de que el mejor trabajador influya en los demás, por lo que cada integrante mejorará y tendrá el nivel de rendimiento de este mejor trabajador. Estos grupos deben tomarse de forma consecutiva, para evitar desórdenes mayores. Su programa debería retornar, en pares, desde qué integrante hasta que integrante comienza cada uno de los grupos formados, de tal forma de que se maximice la suma total de niveles de cada uno de los trabajadores una vez los grupos sean conformados.

## Formato de entrada
| **Formato de entrada** | **Formato de salida** |
| ---------------------- | --------------------- |
| N K                    | A*0* B*0*                 |
| T*0*                     | A*1* B*1*                 |
| T*1*                     | …                     |
| …                      | A*R-1* B*R-1*             |
| T*n-1*                   |                       | 

- N  es el número de personas
- K es el número máximo de trabajadores por grupo
- 𝑇*i* es la capacidad del i-ésimo trabajador
- R es el número de grupos
- 𝐴*i* es el primer integrante del grupo
- 𝐵*i* es el último integrante del grupo
- Siempre debe cumplirse 𝐵*i*−1 + 1 = 𝐴*i*

## Consideración
El programa debe ser capaz de leer un archivo input.txt con el formato descrito en el ejercicio y escribir en un archivo output.txt con el formato descrito en el ejercicio.

## Ejemplo

| **Entrada** | **Salida** |
| ----------- | ---------- |
| 7 3         | 1 3        |
| 1           | 4 4        |
| 15          | 5 7        |
| 7           |            |
| 9           |            |
| 2           |            |
| 5           |            |
| 10            |            |

**Explicación:** Se formaron 3 grupos, los cuales van desde:
1. el trabajador 1 hasta el 3
2. el trabajador 4
3. el trabajador 5 hasta el 7

Si ponemos los niveles de rendimiento que tienen una vez se conformaron los grupos, tenemos: 15 + 15 + 15 + 9 + 10 + 10 + 10 = 84 Esta conformación de grupos maximiza la suma de rendimientos.

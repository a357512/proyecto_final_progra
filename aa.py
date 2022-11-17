import streamlit as st
 
st.title('Aplicación de la salud')
#st.sidebar.button('click here')
#co1, co2= st.sidebar.columns( [2,2] )
#co1.write('esta es la columna 1')
st.sidebar.header('Desliza para seleccionar el número de vasos de agua que tomas por día \N{DROPLET}')
vasoagua= st.sidebar.slider('',0,15)
if vasoagua == 0:
 st.sidebar.write('Ingrese un número entero')
if (vasoagua > 1 and vasoagua < 5):
 st.sidebar.write('Deberías de consumir más agua :c')
if vasoagua == 1:
 st.sidebar.write('Deberías de consumir más agua :c')
if vasoagua == 5:
 st.sidebar.write('Deberías de consumir más agua :c')
if (vasoagua > 6 and vasoagua < 10):
 st.sidebar.write('Perfecto sigue así')
if vasoagua == 6:
 st.sidebar.write('Perfecto sigue así')
if vasoagua == 10:
 st.sidebar.write('Perfecto sigue así')
if (vasoagua > 11 and vasoagua < 20):
 st.sidebar.write('Cuida la cantidad de agua que consumes, puedes estar deshidratado')
if vasoagua == 11:
 st.sidebar.write('Cuida la cantidad de agua que consumes, puedes estar deshidratado')
if vasoagua == 20:
 st.sidebar.write('Cuida la cantidad de agua que consumes, puedes estar deshidratado')

st.sidebar.header('**¿Sabías qué...?**')
st.sidebar.write('En México, el 70% de los mexicanos padece sobrepeso y casi una tercera parte sufre de obesidad, además, esta enfermedad se asocia principalmente con la diabetes y enfermedades cardiovasculares, pero también con trastornos óseos y musculares y algunos tipos de cáncer.')
st.sidebar.write('_ISSSTE, 2016_')
st.sidebar.image('https://sebbm.es/wp-content/uploads/la-obesidad.jpeg')




estatura= st.number_input('Ingrese su estatura en metros',0.01)
masa= st.number_input('Ingrese su masa en kilos',0.01)
imc= masa/estatura**2
x= round(imc,2)
st.title('Tu índice de masa corporal es:')
st.title(x)
if imc ==100:
 st.write('Favor de ingresar su altura y su peso')
 
if imc < 18.5:
  st.write('IMC está por debajo del saludable')
  st.image('https://www.colchonescefiro.es/blog/wp-content/uploads/2015/10/personas-imc-bajo.png')
  st.write('Las personas con esta condición pueden tener un sistema inmunológico débil, así como una pobre condición física, haciéndolos propensos a padecer infecciones. Otros riesgos que puede causar el bajo peso son: Problemas de fertilidad, especialmente en mujeres. También problemas durante el embarazo.')
  st.write('_Top Doctors España_')
  st.subheader('Recomendación')
  st.write('Agregue calorías saludables. Se pueden aumentar las calorías agregando coberturas de nueces o semillas, queso y guarniciones saludables como con almendras, semillas de girasol, frutas o tostadas de trigo integral.')
if (imc>18.5 and imc<24.9):
  st.write('IMC saludable')
  st.image('https://www.colchonescefiro.es/blog/wp-content/uploads/2015/10/personas-imc-medio.png')
  st.write('Su índice de masa corporal indica que está saludable, mantenga sus hábitos saludables para conservar su IMC saludable')
  st.subheader('Recomendación')
  st.write('Al día realiza mínimo 30 minutos de actividad deportiva, haz estiramientos que favorecen a tu circulación.')
if (imc>25 and imc<29.9):
  st.write('IMC indica sobrepeso')
  st.image('https://www.colchonescefiro.es/blog/wp-content/uploads/2015/10/personas-imc-alto.png')
  st.write('El sobrepeso no es una enfermedad, pero es una condición que predispone al desarrollo de enfermedades tales como diabetes, presión elevada (hipertensión), elevación de grasas en sangre (dislipidemias), infartos, embolias, algunos tipos de cáncer y favorece la muerte prematura')
  st.write('_SEMAR, s.f._')
  st.subheader('Recomendación')
  st.write('Disminuye en tu dieta la carne grasa, la mantequilla, el aceite de palma; las comidas procesadas como pizzas congeladas, galletas, snacks de paquete, entre otros.')         
 
 
 
 
if (imc>30 and imc<39.9):
  st.write('IMC indica obesidad')
  st.image('https://www.colchonescefiro.es/blog/wp-content/uploads/2015/10/personas-imc-alto.png')
  st.write('La obesidad es una enfermedad crónica, producida por el consumo excesivo de grasas, azúcares y carbohidratos, lo que provoca la acumulación de grasa en nuestro cuerpo. Otra causa es la poca o nula actividad física en la vida diaria.')
  st.write('_Presidencia de la República EPN, 2013_')
  st.subheader('Recomendación')
  st.write('Establece horarios al comer. Procura comer tus alimentos al horno, salteados, y no fritos. Reducir el consumo de azúcar. Reducir el consumo de sal.')
if imc >40 and imc<99.99:
  st.write('IMC indica obesidad mórbida')
  st.image('https://www.colchonescefiro.es/blog/wp-content/uploads/2015/10/personas-imc-alto.png')
  st.write('Las personas con obesidad mórbida frecuentemente presentan hipertensión arterial, diabetes mellitus, cardiopatía coronaria, insuficiencia respiratoria y dislipidemia; además de lo anterior, pueden padecer limitaciones físicas para realizar actividades debido a problemas osteoarticulares derivados de la obesidad extrema.')
  st.write('_Secretaria de Salud, 2015_')
  st.subheader('Recomendación')
  st.write('Consulta a tu nutriólogo')
  st.write('Correo nutriólog FCQ UACH: ')
if imc >100.01:
 st.write('IMC indica obesidad mórbida')
 st.image('https://www.colchonescefiro.es/blog/wp-content/uploads/2015/10/personas-imc-alto.png')
 st.write('Las personas con obesidad mórbida frecuentemente presentan hipertensión arterial, diabetes mellitus, cardiopatía coronaria, insuficiencia respiratoria y dislipidemia; además de lo anterior, pueden padecer limitaciones físicas para realizar actividades debido a problemas osteoarticulares derivados de la obesidad extrema.')
 st.write('_Secretaria de Salud, 2015_')

st.header('Sección de datos curiosos')
st.write('Oprime para descubrir')
co1, co2, co3, co4, co5 = st.columns( [2,2,2,2,2] )

if co1.button('1'):
  st.subheader('¿Sabías qué?')
  st.write('México ocupa el primer lugar, con mayor número de casos de obesidad infantil.')
  st.write('_Cruz Roja Mexicana, 2021_')
  st.image('https://pbs.twimg.com/media/EYHP9SgU4AEFPpL.jpg:large')

if co2.button('2'):
  st.subheader('¿Sabías qué?')
  st.write('Debes incluir en todas tus comidas del día una fruta o verdura; un cereal o leguminosa y productos de origen animal, además de beber dos litros (8 vasos) de agua.')
  st.write('_Secretaria de Salud, 2015_')
  st.image('https://www.gob.mx/cms/uploads/image/file/489745/plato_bien_comer_2.jpg')
if co3.button('3'):
  st.subheader('¿Sabías qué?')
  st.write('Una de cada 5 muertes en el país es causada por diabetes, enfermedad asociada a la obesidad.')
  st.write('_Secretaria de Salud, 2015_')
  st.image('https://cloudfront-us-east-1.images.arcpublishing.com/infobae/ME3ZPCNI4RFLLFREDVLMDMAKXI.jpg')
if co4.button('4'):
  st.subheader('¿Sabías qué?')
  st.write('Debemos realizar al menos 30 minutos diarios de actividad física. La actividad física es todo movimiento del cuerpo en el que se requiere más energía comparada con el reposo, y puede ser caminar, correr, bailar, nadar, practicar yoga, podar el jardín, entre otros.')
  st.write('_Secretaria de Salud, 2015_')
  st.image('https://www.gob.mx/cms/uploads/article/main_image/97531/IMG-20200708-WA0005.jpg')

co5.button('Borrar selección')

# -*- coding: utf-8 -*-
"""
questions_part1.py - Questions for:
- Bernanke (20)
- Currency School (20)
- Banking School (20)
- McKinnon & Shaw (20)
- Olivera & Canavese (20)
Total: 100 questions.
"""

bank_part1 = {}

# -------------------------------------------------------------
# 4. BEN S. BERNANKE (& GERTLER / GILCHRIST) (20 preguntas)
# -------------------------------------------------------------
bank_part1["bernanke"] = [
    {
        "id": "bernanke_1",
        "question": "¿Cuál es la crítica central que formula Ben Bernanke a la visión tradicional del dinero como simple agregado cuantitativo (M1/M2)?",
        "options": [
            "Que no considera el oro en las reservas internacionales.",
            "Que ignora que en el sistema moderno la variable crítica para la actividad real es la oferta total de crédito bancario y las condiciones de intermediación.",
            "Que M2 debería incluir exclusivamente a las criptomonedas y dinero digital.",
            "Que la velocidad del dinero es matemáticamente imposible de calcular."
        ],
        "correct_index": 1,
        "explanation": "Bernanke enfatiza que los bancos no son simples conductos pasivos de billetes: su función esencial es crear y canalizar crédito. La salud de los balances bancarios y el volumen de préstamos determinan el impacto en la economía real."
    },
    {
        "id": "bernanke_2",
        "question": "¿Qué fricciones fundamentales caracterizan al mercado de crédito según la Nueva Economía Keynesiana de Bernanke?",
        "options": [
            "Rigideces salariales en el sector público.",
            "Asimetrías de información: selección adversa, riesgo moral y costos de monitoreo o de agencia.",
            "Leyes antimonopolio que limitan la apertura de sucursales.",
            "La convertibilidad forzosa de los depósitos en lingotes de plata."
        ],
        "correct_index": 1,
        "explanation": "Los prestamistas enfrentan información imperfecta sobre la solvencia real y la conducta de los deudores (selección adversa y riesgo moral), lo que genera costos de agencia y necesidad de colateral."
    },
    {
        "id": "bernanke_3",
        "question": "¿Cuál es la función social y productiva indispensable que cumplen los bancos comerciales según Bernanke?",
        "options": [
            "Emitir billetes de curso legal en competencia libre.",
            "Resolver fallas de información evaluando proyectos, exigiendo colateral y monitoreando deudores a través de relaciones de largo plazo.",
            "Garantizar que la tasa de interés real sea siempre igual a cero.",
            "Financiar el déficit presupuestario del gobierno federal sin cobrar intereses."
        ],
        "correct_index": 1,
        "explanation": "Los bancos acumulan capital de información crediticia especializado (relationship lending), reduciendo el costo de intermediación para prestatarios que no pueden emitir bonos en el mercado abierto."
    },
    {
        "id": "bernanke_4",
        "question": "Según el modelo de Diamond y Dybvig (1983) destacado por Bernanke, ¿por qué los bancos comerciales son inherentemente vulnerables a pánicos y corridas bancarias?",
        "options": [
            "Porque sus gerentes carecen de capacitación financiera universitaria.",
            "Porque realizan transformación de vencimientos: financian activos ilíquidos a largo plazo con pasivos líquidos exigibles de inmediato.",
            "Porque el Banco Central no les permite cobrar comisiones por transferencias.",
            "Porque sus inversiones se concentran exclusivamente en deuda soberana extranjera."
        ],
        "correct_index": 1,
        "explanation": "Los bancos ofrecen liquidez inmediata a los depositantes mientras prestan a proyectos productivos ilíquidos de largo plazo. Si los depositantes temen por la solvencia y retiran fondos masivamente, se desata una corrida destructiva."
    },
    {
        "id": "bernanke_5",
        "question": "¿Cómo define Bernanke la 'Prima de Financiamiento Externo' (External Finance Premium)?",
        "options": [
            "El interés cobrado por el Fondo Monetario Internacional a países deudores.",
            "La diferencia entre el costo de solicitar fondos prestados a terceros y el costo de oportunidad de financiarse con fondos propios internos.",
            "El impuesto que pagan los bancos comerciales por emitir certificados de depósito.",
            "La rentabilidad adicional que rinden los bonos del tesoro respecto a las acciones."
        ],
        "correct_index": 1,
        "explanation": "La prima de financiamiento externo compensa al prestamista por los costos de agencia y riesgo de default. Cuanto peor es la situación financiera del prestatario, mayor es esta prima."
    },
    {
        "id": "bernanke_6",
        "question": "En el mecanismo del 'Acelerador Financiero' (Bernanke, Gertler y Gilchrist, 1999), ¿cómo se relaciona la prima de financiamiento externo con el colateral del deudor?",
        "options": [
            "Varía en forma directamente proporcional a la tasa de inflación.",
            "Varía inversamente con la riqueza neta y el valor del colateral del deudor.",
            "Es constante e independiente de los balances de las empresas.",
            "Depende exclusivamente de los tipos de cambio flotantes."
        ],
        "correct_index": 1,
        "explanation": "A mayor riqueza neta y valor de los activos del deudor (mayor colateral), menor es el riesgo para el banco y más baja la prima de financiamiento externo, abaratando el crédito."
    },
    {
        "id": "bernanke_7",
        "question": "¿Cómo amplifica el Acelerador Financiero una recesión económica originada por un shock negativo?",
        "options": [
            "La recesión deprime precios de activos $\\rightarrow$ cae el valor del colateral $\\rightarrow$ se dispara la prima de riesgo $\\rightarrow$ se raciona el crédito $\\rightarrow$ la recesión se profundiza.",
            "Aumenta la inversión física al abaratarse los bienes de capital en remate judicial.",
            "Los bancos disminuyen los requisitos de garantías crediticias para reactivar el mercado.",
            "Se produce una expansión automática de la base monetaria en los mercados bursátiles."
        ],
        "correct_index": 0,
        "explanation": "Espiral procíclica del acelerador: la caída de ventas deteriora los balances de firmas y familias; al depreciarse sus colaterales, los bancos suben la prima de riesgo o cortan el crédito, desplomando la inversión."
    },
    {
        "id": "bernanke_8",
        "question": "En su célebre artículo de 1983 sobre la Gran Depresión de 1929, ¿cuál es la gran corrección y aporte que formula Bernanke frente a Friedman y Schwartz?",
        "options": [
            "Demuestra que la cantidad de dinero no tuvo ningún papel en la crisis.",
            "Prueba que la depresión fue prolongada y severa debido al colapso del proceso de intermediación bancaria y la destrucción de información crediticia, no solo a la caída de M1.",
            "Sostiene que la Gran Depresión fue causada por el desempleo tecnológico en la agricultura.",
            "Afirma que la Reserva Federal actuó de forma perfecta y que la crisis provino de Europa."
        ],
        "correct_index": 1,
        "explanation": "Aporte cumbre de Bernanke: la quiebra masiva de miles de bancos destruyó las relaciones de crédito y la información acumulada. Reconstruir este capital informacional llevó una década, explicando la duración de la crisis."
    },
    {
        "id": "bernanke_9",
        "question": "¿Por qué la quiebra de bancos comerciales solventes genera una pérdida irreversible de capital informacional según Bernanke?",
        "options": [
            "Porque los bancos queman sus archivos contables durante los procesos de liquidación.",
            "Porque los bancos supervivientes no conocen el historial crediticio de los clientes de los bancos fallidos y les niegan o encarecen el financiamiento.",
            "Porque los depositantes emigran al extranjero llevándose sus ahorros.",
            "Porque la ley prohíbe fundar nuevos bancos durante los siguientes veinte años."
        ],
        "correct_index": 1,
        "explanation": "El conocimiento sobre la solvencia moral y comercial de una pyme reside en el banco con el que opera hace años. Si ese banco quiebra, las demás entidades racionan el crédito por asimetría de información."
    },
    {
        "id": "bernanke_10",
        "question": "En su conferencia Nobel de 2022, ¿cómo define Bernanke el epicentro de la Gran Crisis Financiera de 2008?",
        "options": [
            "Como una crisis clásica de billetes de baja denominación.",
            "Como una corrida bancaria análoga a la de 1929, pero ocurrida en el sistema bancario paralelo o 'Shadow Banking' (mercados de repos y papeles comerciales).",
            "Como una huelga general de los trabajadores de la construcción.",
            "Como una crisis fiscal de sobreendeudamiento del Tesoro estadounidense."
        ],
        "correct_index": 1,
        "explanation": "En 2008 la corrida no fue en ventanillas minoristas aseguradas por el FDIC, sino en el Shadow Banking mayorista (repos y commercial paper a 24 horas garantizados con activos subprime). Al desconfiar del colateral, el fondeo se cortó de golpe."
    },
    {
        "id": "bernanke_11",
        "question": "¿Qué instrumento no convencional aplicó Ben Bernanke al frente de la Fed cuando la tasa de interés tocó el límite inferior de cero (Zero Lower Bound)?",
        "options": [
            "La confiscación obligatoria del 10% de los saldos bancarios de las familias.",
            "La Flexibilización Cuantitativa (Quantitative Easing - QE): compra masiva de activos financieros de largo plazo para comprimir primas por plazo y restaurar liquidez.",
            "La fijación de precios máximos en los supermercados de todo el país.",
            "La suspensión del patrón dólar en el comercio internacional."
        ],
        "correct_index": 1,
        "explanation": "El QE consistió en expandir el balance de la Fed comprando masivamente títulos del Tesoro de largo plazo y bonos respaldados por hipotecas (MBS) para bajar las tasas largas y desbloquear el mercado de crédito."
    },
    {
        "id": "bernanke_12",
        "question": "¿Cómo actualiza Bernanke la clásica 'Doctrina de Bagehot' para la gestión de pánicos sistémicos modernos?",
        "options": [
            "El Banco Central debe prestar únicamente a empresas de aviación comercial.",
            "El Prestamista de Última Instancia debe suministrar liquidez de forma irrestricta a entidades solventes contra buen colateral pero a tasas de penalización, extendiéndose al Shadow Banking.",
            "Se debe cerrar la bolsa de valores durante un año hasta que los precios se estabilicen.",
            "El Banco Central debe negarse a rescatar a cualquier entidad para dar un ejemplo moral."
        ],
        "correct_index": 1,
        "explanation": "Bagehot (1873) prescribía prestar libremente contra buen colateral y a tasas punitivas. Bernanke extendió este principio a bancos de inversión y fondos mutuos del mercado monetario en 2008 para frenar el contagio sistémico."
    },
    {
        "id": "bernanke_13",
        "question": "¿Qué objetivo persigue la política de 'Orientación hacia adelante' (Forward Guidance) aplicada por Bernanke?",
        "options": [
            "Fijar el precio oficial de los combustibles con seis meses de anticipación.",
            "Gestionar las expectativas del público comprometiéndose a mantener bajas las tasas de interés futuras hasta alcanzar metas concretas de desempleo e inflación.",
            "Orientar el crédito bancario exclusivamente hacia la industria automotriz.",
            "Prohibir que los bancos comerciales repartan dividendos a sus accionistas."
        ],
        "correct_index": 1,
        "explanation": "Al comunicar de forma creíble que las tasas cortas seguirán en cero durante un período prolongado, el Banco Central logra reducir las tasas de interés de mediano y largo plazo en toda la economía."
    },
    {
        "id": "bernanke_14",
        "question": "¿Por qué Bernanke aboga por regulaciones macroprudenciales además de la política monetaria tradicional?",
        "options": [
            "Porque la política monetaria tradicional con tasas de interés es un instrumento demasiado tosco que no puede desinflar burbujas en sectores específicos sin dañar a toda la economía.",
            "Porque los bancos centrales no tienen facultad para imprimir billetes sin permiso de los bancos privados.",
            "Porque las regulaciones macroprudenciales sustituyen la necesidad de cobrar impuestos tributarios ordinarios.",
            "Porque la inflación es un fenómeno que solo afecta a los países en desarrollo."
        ],
        "correct_index": 0,
        "explanation": "Subir la tasa de interés general para frenar una burbuja inmobiliaria generaría recesión en todos los demás sectores. Es más eficiente usar herramientas micro y macroprudenciales específicas (límites loan-to-value, buffers de capital)."
    },
    {
        "id": "bernanke_15",
        "question": "¿En qué consisten los colchones o amortiguadores de capital contracíclicos introducidos bajo el régimen de Basilea III?",
        "options": [
            "En exigir que los bancos acumulen capital propio excedente durante fases de auge crediticio para absorber pérdidas durante las recesiones.",
            "En obligar a los bancos a comprar acciones de empresas en quiebra.",
            "En prohibir que los bancos comerciales tengan clientes extranjeros.",
            "En transferir las ganancias bancarias a las arcas del Tesoro público cada mes."
        ],
        "correct_index": 0,
        "explanation": "Para evitar que los bancos tengan que contraer violentamente el crédito durante las crisis, se les obliga a acumular un colchón de capital adicional durante los años de bonanza que amortigüe el deterioro del balance."
    },
    {
        "id": "bernanke_16",
        "question": "¿Qué es una 'Prueba de Estrés' (Stress Test) bancaria implementada por la Reserva Federal tras la crisis de 2008?",
        "options": [
            "Un examen médico y psicológico obligatorio a los empleados bancarios.",
            "Una simulación cuantitativa rigurosa para verificar si el capital de los bancos resistiría escenarios hipotéticos de severa recesión, desempleo y caída de precios de activos.",
            "Una inspección física a las bóvedas de los bancos para contar los billetes en caja.",
            "Un control de precios sobre las tasas de las tarjetas de crédito."
        ],
        "correct_index": 1,
        "explanation": "El Comprehensive Capital Analysis and Review (CCAR) evalúa si las grandes instituciones financieras mantendrían niveles suficientes de capital para seguir prestando bajo escenarios de crisis catastrófica simulada."
    },
    {
        "id": "bernanke_17",
        "question": "¿Cómo se resuelve el problema de las entidades 'Demasiado Grandes para Quebrar' (Too Big To Fail) en la arquitectura financiera post-2008?",
        "options": [
            "Garantizando por ley que el Estado pagará todas las deudas de los accionistas sin excepción.",
            "Mediante regímenes de resolución ordenada (como el Título II de Dodd-Frank) que permiten liquidar una entidad sistémica imponiendo pérdidas a accionistas y acreedores sin rescate público.",
            "Dividiendo a cada banco en quinientas microentidades independientes.",
            "Prohibiendo a las empresas cotizar en los mercados de valores de Wall Street."
        ],
        "correct_index": 1,
        "explanation": "Para evitar el riesgo moral de rescates con dinero de los contribuyentes, se crearon marcos legales para reestructurar o liquidar bancos gigantes de forma ordenada, absorbiendo pérdidas el capital privado (bail-in)."
    },
    {
        "id": "bernanke_18",
        "question": "¿Cuál es la diferencia entre el canal tradicional de las tasas de interés y el canal del préstamo bancario de Bernanke?",
        "options": [
            "El canal tradicional opera a través de los depósitos en cuenta corriente; el canal del préstamo no existe en economías abiertas.",
            "El canal tradicional opera por la reducción del costo de capital en bonos; el canal del préstamo opera alterando directamente la oferta física de créditos que los bancos otorgan a empresas dependientes de crédito bancario.",
            "El canal tradicional fue formulado por Adam Smith y el canal del préstamo por David Ricardo.",
            "Ambos canales son matemáticamente equivalentes bajo cualquier circunstancia empírica."
        ],
        "correct_index": 1,
        "explanation": "El canal del préstamo demuestra que la política monetaria no solo mueve la tasa de interés general, sino que afecta la disponibilidad de financiamiento para pequeñas y medianas empresas que no tienen acceso a emitir bonos en el mercado de capitales."
    },
    {
        "id": "bernanke_19",
        "question": "¿Por qué Bernanke sostiene que la deflación de precios es sumamente peligrosa para la estabilidad del sistema bancario?",
        "options": [
            "Porque la deflación abarata el costo de vida de los trabajadores.",
            "Porque eleva el valor real de las deudas nominales vigentes (deflación por deuda de Fisher), deteriorando la capacidad de pago de los deudores y multiplicando los impagos bancarios.",
            "Porque el Banco Central debe imprimir billetes con números negativos.",
            "Porque estimula un aumento descontrolado de las importaciones extranjeras."
        ],
        "correct_index": 1,
        "explanation": "Como los contratos de crédito se pactan en términos nominales rígidos, la deflación eleva la carga real de la deuda de familias y firmas, desatando olas de cesación de pagos que quiebran a los bancos."
    },
    {
        "id": "bernanke_20",
        "question": "¿Qué paralelismo conceptual existe entre la teoría del canal del crédito de Bernanke y la hipótesis de represión financiera de McKinnon?",
        "options": [
            "Ambos postulan que el oro debe respaldar en un 100% los depósitos bancarios.",
            "Ambos demuestran que cuando la infraestructura y la intermediación bancaria se deterioran o se atrofian, la economía real sufre una contracción severa en su inversión y productividad.",
            "Ambos sostienen que el dinero es un velo neutral que no tiene efectos reales en ningún horizonte temporal.",
            "Ambos recomiendan nacionalizar el comercio exterior de granos."
        ],
        "correct_index": 1,
        "explanation": "Coincidencia fundamental: tanto Bernanke (en economías industriales) como McKinnon (en emergentes) prueban que los bancos son el motor de la inversión; si los canales de crédito colapsan, la actividad productiva se estrangula."
    }
]

# -------------------------------------------------------------
# 5. CURRENCY SCHOOL (RICARDO, OVERSTONE, TORRENS) (20 preguntas)
# -------------------------------------------------------------
bank_part1["currency_school"] = [
    {
        "id": "currency_1",
        "question": "¿Cuál es la definición estricta de dinero adoptada por la Currency School en los debates británicos del siglo XIX?",
        "options": [
            "Cualquier instrumento financiero que rinda intereses en el mercado de Londres.",
            "Única y exclusivamente las monedas y lingotes de oro físico, y los billetes de banco que operan como certificados de respaldo directo de dicho metal.",
            "La suma agregada de depósitos bancarios a la vista, pagarés y letras de cambio comerciales.",
            "El crédito fiduciario emitido sin límite por las compañías navieras."
        ],
        "correct_index": 1,
        "explanation": "Para la Currency School, el único dinero auténtico es el dinero metálico y los billetes que funcionan como certificados de oro al 100%. Descartan de cuajo que los cheques o depósitos bancarios sean dinero."
    },
    {
        "id": "currency_2",
        "question": "¿Por qué la Currency School rechazaba considerar a los depósitos bancarios en cuenta corriente y a las letras de cambio como dinero?",
        "options": [
            "Porque eran emitidos en moneda extranjera francesa o española.",
            "Porque los consideraban meros instrumentos de crédito auxiliares que economizan el uso del dinero, pero que carecen de la cualidad intrínseca de dinero definitivo.",
            "Porque estaban prohibidos por la Iglesia Anglicana de Inglaterra.",
            "Porque no tenían valor nominal impreso en la superficie del papel."
        ],
        "correct_index": 1,
        "explanation": "Sostenían que los cheques y letras son promesas de pago o créditos que ayudan a circular bienes, pero que deben liquidarse finalmente en moneda genuina (oro o billetes del Banco de Inglaterra)."
    },
    {
        "id": "currency_3",
        "question": "Según la Currency School, ¿cuál es la causa motriz de la inflación interna y de la depreciación de la libra esterlina?",
        "options": [
            "Las malas cosechas de trigo en el continente europeo.",
            "La sobreemisión de billetes de banco por encima de las reservas de oro metálico existentes en el país.",
            "El aumento de los costos laborales en los telares de Manchester.",
            "La fijación burocrática de aranceles al carbón por parte del Parlamento."
        ],
        "correct_index": 1,
        "explanation": "Postulado clásico de David Ricardo: la pérdida de valor de la moneda y el alza de precios se deben en todo momento al exceso cuantitativo de billetes de banco emitidos sin respaldo en metálico."
    },
    {
        "id": "currency_4",
        "question": "¿Cuál es el mecanismo automático del 'flujo de especies' (especie-drenaje) que describe la Currency School ante una sobreemisión?",
        "options": [
            "La emisión abarata el dinero $\\rightarrow$ suben precios internos $\\rightarrow$ aumentan importaciones $\\rightarrow$ surge déficit comercial $\\rightarrow$ se drena oro hacia el exterior para pagar.",
            "La emisión atrae automáticamente lingotes de oro de las colonias americanas.",
            "El Banco de Inglaterra confisca las cosechas para compensar la balanza de pagos.",
            "Los precios caen instantáneamente restaurando la competitividad exportadora."
        ],
        "correct_index": 0,
        "explanation": "Mecanismo ricardiano: si hay exceso de billetes, los precios domésticos suben. Las mercancías extranjeras se vuelven más atractivas y se genera déficit externo, obligando a exportar oro físico para liquidar la deuda."
    },
    {
        "id": "currency_5",
        "question": "¿Qué juicio ético y económico emitía la Currency School respecto a la reserva fraccionaria practicada por los bancos privados?",
        "options": [
            "La consideraban un invento maravilloso que multiplicaba la riqueza sin límites.",
            "La condenaban severamente, afirmando que permitía a banqueros privados crear dinero artificial para especulación privada a expensas de la estabilidad pública.",
            "Consideraban que debía ser obligatoria en un 1% para todos los bancos comerciales.",
            "Sostenían que la reserva fraccionaria reducía el costo del gasto militar del Imperio."
        ],
        "correct_index": 1,
        "explanation": "Consideraban que conceder la prerrogativa de emitir promesas de pago con reserva fraccionaria a bancos privados con fines de lucro generaba ciclos artificiales de crédito y estafas a los tenedores de billetes."
    },
    {
        "id": "currency_6",
        "question": "¿En qué año se aprobó la célebre 'Bank Charter Act' (Ley Peel) que plasmó en la legislación británica el ideario de la Currency School?",
        "options": [
            "En 1776, tras la independencia de los Estados Unidos.",
            "En 1844, bajo el gobierno del Primer Ministro Robert Peel.",
            "En 1933, durante la administración de Franklin D. Roosevelt.",
            "En 1815, al finalizar las guerras napoleónicas en Waterloo."
        ],
        "correct_index": 1,
        "explanation": "La Ley de Robert Peel fue promulgada en 1844 y representó la victoria parlamentaria absoluta de la Currency School sobre la Banking School en Gran Bretaña."
    },
    {
        "id": "currency_7",
        "question": "¿Qué trascendental reforma orgánica impuso la Ley Peel de 1844 dentro de la estructura del Banco de Inglaterra?",
        "options": [
            "Fusionó el Banco de Inglaterra con la Bolsa de Valores de Londres.",
            "Dividió al Banco de Inglaterra en dos departamentos legalmente independientes: el Departamento de Emisión y el Departamento Bancario.",
            "Eliminó por completo la Junta de Gobernadores del Banco Central.",
            "Transformó al Banco de Inglaterra en una sociedad anónima de propiedad de los sindicatos."
        ],
        "correct_index": 1,
        "explanation": "La ley separó de raíz la función monetaria de la bancaria: el Issue Department (Departamento de Emisión) custodiaba el oro y emitía billetes; el Banking Department (Departamento Bancario) operaba como un banco comercial común."
    },
    {
        "id": "currency_8",
        "question": "¿Cuál fue el monto fiduciario máximo fijado por la Ley Peel de 1844 que el Departamento de Emisión podía respaldar en títulos del gobierno sin oro?",
        "options": [
            "100 millones de libras esterlinas.",
            "14 millones de libras esterlinas.",
            "Cero libras esterlinas (prohibición fiduciaria absoluta).",
            "500 mil libras esterlinas."
        ],
        "correct_index": 1,
        "explanation": "Se autorizó una emisión fiduciaria respaldada en deuda pública de exactamente £14 millones para cubrir las transacciones mínimas históricas; por encima de ese monto, cada libra debía estar respaldada 100% en oro."
    },
    {
        "id": "currency_9",
        "question": "¿Qué exigía la Ley Peel de 1844 para cualquier emisión de billetes que superara el límite fiduciario de los £14 millones?",
        "options": [
            "La aprobación previa de la Cámara de los Comunes en sesión secreta.",
            "Un respaldo estricto del 100% en reservas de oro físico depositadas en las bóvedas del Departamento de Emisión.",
            "Un respaldo en acciones de las empresas de ferrocarriles británicas.",
            "Que los billetes fueran distribuidos exclusivamente a campesinos de Irlanda."
        ],
        "correct_index": 1,
        "explanation": "El Principio de la Moneda: todo billete adicional emitido por encima del cupo fiduciario debía tener una contrapartida exacta de una libra de oro en la bóveda, garantizando una equivalencia metálica perfecta."
    },
    {
        "id": "currency_10",
        "question": "¿Cuál era el principio operativo ideal que perseguía la Currency School para la circulación monetaria británica?",
        "options": [
            "Que la oferta monetaria fuera gestionada de manera totalmente flexible por economistas tecnócratas.",
            "El Principio de la Circulación Metálica: que el papel moneda fluctuara de forma mecánica y automática exactamente como si fuera una moneda metálica pura.",
            "Que la cantidad de dinero creciera al 15% anual para subsidiar las exportaciones coloniales.",
            "Que los bancos comerciales emitieran billetes de diferentes colores según la estación climática."
        ],
        "correct_index": 1,
        "explanation": "Objetivo declarado: lograr que la moneda mixta (papel y metal) varíe en volumen exactamente igual a como habría variado si la circulación consistiera exclusivamente en monedas de oro."
    },
    {
        "id": "currency_11",
        "question": "¿Qué papel asignaba la Currency School a la discrecionalidad de los directores del Banco de Inglaterra?",
        "options": [
            "El rol de diseñar políticas activas de fomento industrial con tipos de cambio múltiples.",
            "Cero discrecionalidad: el Departamento de Emisión debía actuar como un autómata mecánico de canje de oro por billetes.",
            "La facultad de modificar el encaje bancario trimestralmente según el índice de desempleo.",
            "El monopolio de fijar las tasas de interés de todas las hipotecas urbanas."
        ],
        "correct_index": 1,
        "explanation": "Eliminación total del juicio discrecional: ningún banquero debía tener el poder de decidir cuánto dinero emitir. La oferta monetaria debía ser determinada exclusivamente por los flujos de la balanza de pagos."
    },
    {
        "id": "currency_12",
        "question": "En el marco de la Currency School, ¿cómo se originan los ciclos de auge y caída comercial (Boom and Bust)?",
        "options": [
            "Por el impacto de manchas solares sobre el rendimiento de las cosechas mundiales.",
            "Por expansiones crediticias artificiales y no respaldadas de los bancos emisores que generan burbujas y posterior drenaje de reservas de oro.",
            "Por conspiraciones diplomáticas de las potencias navales rivales.",
            "Por la escasez de mano de obra en las minas de carbón de Gales."
        ],
        "correct_index": 1,
        "explanation": "El auge artificial se gesta cuando los bancos expanden billetes sin respaldo a tasas bajas; la especulación sube los precios hasta que el déficit comercial drena el oro forzando una contracción súbita que causa la quiebra comercial."
    },
    {
        "id": "currency_13",
        "question": "¿Qué antecedente histórico del siglo XX se nutrió directamente de los principios de la Currency School?",
        "options": [
            "El Plan Chicago de 1933 que proponía un encaje bancario del 100% sobre los depósitos a la vista.",
            "El Plan Marshall para la reconstrucción de la posguerra europea.",
            "El New Deal fiscal de Franklin D. Roosevelt.",
            "La creación del Banco Central Europeo bajo el Tratado de Maastricht."
        ],
        "correct_index": 0,
        "explanation": "El '100% Money Plan' ideado por Irving Fisher y economistas de Chicago en los años 30 para separar el dinero del crédito es la reencarnación moderna del principio de la Ley Peel de 1844."
    },
    {
        "id": "currency_14",
        "question": "¿Con qué movimiento contemporáneo de reforma monetaria europea se relaciona la doctrina de la Currency School?",
        "options": [
            "Con la Teoría Monetaria Moderna (MMT).",
            "Con el movimiento de Dinero Soberano (Vollgeld / Sovereign Money), que busca abolir la creación bancaria de dinero privado.",
            "Con las doctrinas de flexibilización cuantitativa de Mario Draghi.",
            "Con las propuestas de moneda común del Mercosur."
        ],
        "correct_index": 1,
        "explanation": "La iniciativa suiza de Dinero Soberano (Vollgeld) y las tesis de Positive Money retoman el postulado de la Currency School: el Estado debe tener el monopolio exclusivo del 100% del dinero, eliminando la creación de dinero bancario comercial."
    },
    {
        "id": "currency_15",
        "question": "¿Cuál fue el fallo institucional fatal que exhibió la Ley Peel en la práctica real cuando estallaron pánicos de liquidez?",
        "options": [
            "Que provocó hiperinflaciones inmediatas en Gran Bretaña.",
            "Que al prohibir al Banco de Inglaterra emitir billetes sin oro, la ley provocó una parálisis total de liquidez que forzó a suspender la ley en 1847, 1857 y 1866.",
            "Que el oro fue robado de las bóvedas del Banco de Inglaterra.",
            "Que los comerciantes se negaron a aceptar monedas de oro en las transacciones."
        ],
        "correct_index": 1,
        "explanation": "Paradoja de la Ley Peel: ante un pánico, el público deseaba billetes del Banco de Inglaterra. Como el oro se drenaba, el banco no podía emitir, amenazando con la quiebra a todo el comercio solvente hasta que el gobierno suspendió la ley de emergencia."
    },
    {
        "id": "currency_16",
        "question": "¿Qué ocurría cada vez que el gobierno británico emitía una 'Carta del Canciller' suspendiendo temporalmente la Ley Peel?",
        "options": [
            "La libra esterlina perdía el 90% de su valor en los mercados cambiarios.",
            "Se autorizaba al Banco de Inglaterra a emitir billetes sin respaldo de oro, lo que calmaba el pánico de forma instantánea.",
            "Se clausuraba el Parlamento británico por tiempo indefinido.",
            "Los bancos comerciales eran expropiados por la Corona."
        ],
        "correct_index": 1,
        "explanation": "El mero anuncio de que el Banco de Inglaterra quedaba legalmente facultado para suministrar liquidez ilimitada extinguía de inmediato la corrida bancaria, confirmando las advertencias de la rival Banking School."
    },
    {
        "id": "currency_17",
        "question": "¿Cómo concebía la demanda de dinero David Ricardo y los líderes de la Currency School?",
        "options": [
            "Como una función altamente elástica a la especulación de activos bursátiles.",
            "Como una demanda pasiva fijada de manera rígida por el volumen físico de mercancías comerciadas a velocidad constante.",
            "Como un escudo psicológico contra la angustia del porvenir.",
            "Como una variable gobernada por los sindicatos fabriles."
        ],
        "correct_index": 1,
        "explanation": "Adscribían a la versión clásica más rígida de la teoría cuantitativa: la demanda de dinero es una necesidad puramente técnica para transacciones de mercancías; cualquier dinero adicional emitido es exceso monetario."
    },
    {
        "id": "currency_18",
        "question": "¿Quiénes fueron los principales líderes teóricos de la Currency School frente a la Banking School?",
        "options": [
            "Adam Smith y Karl Marx.",
            "David Ricardo, Samuel Jones Loyd (Lord Overstone) y Robert Torrens.",
            "John Maynard Keynes y Joan Robinson.",
            "Milton Friedman y Anna Schwartz."
        ],
        "correct_index": 1,
        "explanation": "David Ricardo sentó las bases teóricas en sus tratados bullionistas, y Lord Overstone y Robert Torrens articularon la doctrina política que triunfó con Robert Peel en 1844."
    },
    {
        "id": "currency_19",
        "question": "¿Por qué la Currency School desconfiaba profundamente de la 'Doctrina de las Letras Reales' promovida por sus rivales?",
        "options": [
            "Porque sostenía que prestar contra letras comerciales genera una espiral inflacionaria acumulativa de crédito que retroalimenta los precios al alza.",
            "Porque las letras de cambio estaban redactadas en idioma latín.",
            "Porque las letras comerciales eran emitidas únicamente por agricultores pobres.",
            "Porque consideraba que el comercio exterior debía liquidarse mediante trueque de telas por vino."
        ],
        "correct_index": 0,
        "explanation": "Argumento de Overstone y Torrens: si los precios suben, el valor nominal de las letras reales aumenta; los bancos conceden más crédito contra esas letras y los precios suben más, creando una inflación descontrolada."
    },
    {
        "id": "currency_20",
        "question": "¿Qué lección fundamental para la teoría bancaria moderna dejó el experimento histórico de la Ley Peel de 1844?",
        "options": [
            "Que la fijación de reglas cuantitativas rígidas del 100% sin una válvula de escape de prestamista de última instancia conduce inevitablemente al colapso en momentos de crisis sistémica.",
            "Que el oro es un metal tóxico para la salud pública de los cajeros bancarios.",
            "Que el crédito bancario puede eliminarse totalmente por decreto legislativo.",
            "Que la banca libre sin Banco Central es el único sistema financieramente estable."
        ],
        "correct_index": 0,
        "explanation": "La rigidez absoluta de la Ley Peel demostró que un sistema monetario moderno no puede funcionar sin la elasticidad del prestamista de última instancia en situaciones de pánico o estrés de liquidez."
    }
]

# -------------------------------------------------------------
# 6. BANKING SCHOOL (TOOKE, FULLARTON, WILSON) (20 preguntas)
# -------------------------------------------------------------
bank_part1["banking_school"] = [
    {
        "id": "banking_1",
        "question": "¿Cuál es la concepción del dinero defendida por la Banking School frente a la Currency School en el siglo XIX?",
        "options": [
            "El dinero debe ser exclusivamente metálico y emitido por el ejército.",
            "Una concepción amplia y endógena: no existe distinción cualitativa entre billetes de banco, depósitos en cuenta corriente, cheques y letras de cambio comerciales.",
            "El dinero es una ilusión contable inventada por los bancos centrales.",
            "Solo se considera dinero a la deuda pública emitida a perpetuidad."
        ],
        "correct_index": 1,
        "explanation": "Para la Banking School, todos los medios de pago nacidos de la intermediación crediticia (depósitos, cheques, letras) cumplen idéntica función transaccional que los billetes de banco."
    },
    {
        "id": "banking_2",
        "question": "¿Qué postula el principio del 'Dinero Endógeno' introducido por la Banking School y precursor del poskeynesianismo?",
        "options": [
            "Que el dinero es inyectado desde helicópteros por el Banco Central como una variable exógena.",
            "Que 'los préstamos crean depósitos' (Loans create deposits): la oferta de medios de pago es creada por los bancos en respuesta a la demanda de crédito de la economía real.",
            "Que el dinero desaparece cada vez que un comerciante exporta mercancías.",
            "Que los bancos comerciales solo pueden prestar las reservas de oro que previamente les depositaron."
        ],
        "correct_index": 1,
        "explanation": "Los bancos no son simples intermediarios pasivos de ahorros previos: cuando otorgan un préstamo o descuentan una letra, crean un depósito nuevo de la nada (creación de dinero de crédito endógeno)."
    },
    {
        "id": "banking_3",
        "question": "¿Cómo se determina la cantidad de dinero en circulación según la tesis de las 'Necesidades del Comercio' (Needs of Trade)?",
        "options": [
            "Por un sorteo público celebrado anualmente en el Parlamento británico.",
            "De forma pasiva por el sistema bancario, guiado por la demanda solvente de financiamiento y transacciones de los empresarios y comerciantes.",
            "Mediante la extracción física de lingotes de plata en las minas coloniales.",
            "Por un algoritmo matemático rígido supervisado por la Corona británica."
        ],
        "correct_index": 1,
        "explanation": "Para la Banking School, la oferta monetaria se ajusta elásticamente al nivel de actividad: si la economía crece y demanda más crédito, los bancos emiten más depósitos; los bancos no pueden forzar dinero sobre el público."
    },
    {
        "id": "banking_4",
        "question": "En la teoría de la Banking School, ¿en qué dirección fluye la causalidad entre el nivel de precios y la cantidad de dinero?",
        "options": [
            "El dinero causa los precios, como postula la teoría cuantitativa.",
            "Los costos reales de producción y los precios de los bienes determinan la cantidad de dinero demandada y creada por los bancos (causalidad inversa).",
            "No existe ninguna relación estadística ni teórica entre ambas variables.",
            "El tipo de cambio fijo congela tanto precios como saldos monetarios."
        ],
        "correct_index": 1,
        "explanation": "Tooke invierte la causalidad ricardiana: las malas cosechas o salarios elevan los precios de las mercancías; ese nivel más alto de precios induce a los comerciantes a pedir préstamos más grandes, expandiendo la cantidad de dinero."
    },
    {
        "id": "banking_5",
        "question": "¿Por qué Thomas Tooke y John Fullarton afirmaban categóricamente que la emisión de billetes convertibles en oro NO puede causar inflación?",
        "options": [
            "Porque los billetes emitidos estaban bendecidos por la Iglesia de Inglaterra.",
            "Por la vigencia de la 'Ley del Reflujo': cualquier emisión de billetes por encima de las necesidades transaccionales refluye inmediatamente a los bancos emisores.",
            "Porque los comerciantes británicos preferían quemar los billetes sobrantes.",
            "Porque la velocidad del dinero caía automáticamente a cero ante cada emisión."
        ],
        "correct_index": 1,
        "explanation": "Pilar de examen: en un régimen de billetes legalmente convertibles, un banco no puede inundar el mercado con papel moneda; el público no retiene saldos ociosos y el exceso vuelve al banco emisor."
    },
    {
        "id": "banking_6",
        "question": "¿Cuáles son los tres canales concretos mediante los cuales opera la 'Ley del Reflujo' (Law of Reflux) de John Fullarton?",
        "options": [
            "Pago de impuestos aduaneros, multas judiciales y compra de tierras comunales.",
            "Cancelación de préstamos bancarios vencidos, constitución de depósitos bancarios remunerados, y canje por oro físico si se desea atesorar.",
            "Emigración al continente europeo, compra de acciones navieras y destrucción de billetes.",
            "Fijación de precios máximos, congelamiento salarial y subsidios estatales."
        ],
        "correct_index": 1,
        "explanation": "El exceso de billetes refluye al emisor: 1) deudores devuelven préstamos con los billetes sobrantes; 2) ahorristas los depositan a interés; 3) se presentan al banco exigiendo oro metálico."
    },
    {
        "id": "banking_7",
        "question": "¿En qué consiste la 'Doctrina de las Letras Reales' (Real Bills Doctrine) defendida por la Banking School?",
        "options": [
            "En autorizar a los bancos a comprar cuadros y obras de arte reales de la realeza.",
            "En postular que si los bancos descuentan exclusivamente letras de cambio de corto plazo que financian la producción o transporte de bienes reales en movimiento, el crédito nunca generará inflación.",
            "En emitir billetes respaldados en títulos de la deuda externa soberana de España.",
            "En prohibir que los comerciantes otorguen plazos de pago superiores a 24 horas."
        ],
        "correct_index": 1,
        "explanation": "Si el crédito se liga a bienes físicos que en 60 o 90 días llegarán al mercado y cancelarán la letra, la oferta monetaria se auto-regulará con perfecta elasticidad según las necesidades reales sin causar inflación."
    },
    {
        "id": "banking_8",
        "question": "¿Cuál es la crítica que formula la Banking School a la concepción de las crisis de la Currency School?",
        "options": [
            "Que las crisis se deben exclusivamente al exceso de ahorro voluntario.",
            "Que las crisis comerciales no se originan en la sobreemisión de billetes, sino en perturbaciones reales: sobreespeculación en cosechas o materias primas, guerras o caídas en la confianza comercial.",
            "Que las crisis no existen en economías con moneda metálica pura.",
            "Que los bancos comerciales nunca quiebran bajo la Ley Peel."
        ],
        "correct_index": 1,
        "explanation": "Para la Banking School, las crisis se gestan en la economía real y en el optimismo de los negocios; la creación de crédito solo acompaña el ciclo productivo y no es su causa originaria."
    },
    {
        "id": "banking_9",
        "question": "¿Por qué la Banking School pronosticó con éxito que la Ley Peel de 1844 provocaría catástrofes financieras en momentos de pánico?",
        "options": [
            "Porque el oro físico era demasiado pesado para ser transportado.",
            "Porque al fijar una camisa de fuerza rígida de emisión, cuando estallara un pánico y aumentara la demanda de liquidez, la prohibición de emitir estrangularía a los bancos solventes provocando quiebras masivas.",
            "Porque la Cámara de los Comunes aumentaría los impuestos al carbón.",
            "Porque los trabajadores destruirían las máquinas de vapor en protesta."
        ],
        "correct_index": 1,
        "explanation": "Advertencia certera: en un pánico, el comercio demanda desesperadamente billetes del Banco de Inglaterra. Si la ley prohíbe emitirlos porque bajó el oro, se empuja a la suspensión de pagos a comerciantes solventes."
    },
    {
        "id": "banking_10",
        "question": "¿Qué ocurrió en las crisis históricas británicas de 1847, 1857 y 1866 que reivindicó a la Banking School?",
        "options": [
            "El Banco de Inglaterra fue nacionalizado por el Partido Laborista.",
            "El gobierno británico tuvo que suspender de emergencia la Ley Peel para permitir que el Banco de Inglaterra emitiera billetes fiduciarios sin respaldo de oro, frenando el pánico de inmediato.",
            "Gran Bretaña abandonó definitivamente el uso del papel moneda.",
            "La Currency School disolvió el parlamento británico."
        ],
        "correct_index": 1,
        "explanation": "En las tres crisis, el gobierno tuvo que autorizar la suspensión de la Ley Peel. La sola autorización de emitir con flexibilidad restauró la confianza y detuvo el pánico, probando la necesidad de elasticidad monetaria."
    },
    {
        "id": "banking_11",
        "question": "¿Qué rol debe cumplir el Banco de Inglaterra según la concepción de la Banking School?",
        "options": [
            "Ser una agencia recaudadora de impuestos de la Corona.",
            "Actuar como un prestamista elástico y mantener reservas holgadas de oro no para trabar la emisión, sino para amortiguar salidas externas transitorias sin contraer el crédito legítimo.",
            "Prohibir que los bancos privados otorguen créditos comerciales a más de 30 días.",
            "Fijar el precio oficial del trigo y de la cebada."
        ],
        "correct_index": 1,
        "explanation": "Las reservas del Banco Central no deben ser una camisa de fuerza legal para congelar la moneda, sino un colchón de seguridad para absorber shocks de balanza de pagos sin destruir el crédito comercial."
    },
    {
        "id": "banking_12",
        "question": "En la monumental obra 'A History of Prices' (6 volúmenes), ¿qué método científico empleó Thomas Tooke para desafiar a David Ricardo?",
        "options": [
            "Deducciones lógicas puras a priori sin necesidad de contrastación empírica.",
            "La recopilación sistemática e inductiva de series estadísticas históricas de precios de mercancías a lo largo de más de un siglo.",
            "Entrevistas exclusivas a miembros de la familia real británica.",
            "Modelos matemáticos de equilibrio general computado."
        ],
        "correct_index": 1,
        "explanation": "Tooke fundamentó sus tesis en una exhaustiva investigación empírica e histórica, demostrando con datos reales que las fluctuaciones de precios precedían a los cambios monetarios y dependían de cosechas y aranceles."
    },
    {
        "id": "banking_13",
        "question": "¿Por qué la Banking School argumenta que es imposible obligar al público a retener un exceso de billetes de banco convertibles?",
        "options": [
            "Porque el público no sabe leer el valor facial de los billetes.",
            "Porque el público solo retiene los medios de pago que necesita para sus gastos; si le entregan billetes sobrantes, los deposita inmediatamente en los bancos para ganar intereses.",
            "Porque los billetes se degradan físicamente en menos de una semana.",
            "Porque la policía confisca el efectivo que supera los cincuenta chelines."
        ],
        "correct_index": 1,
        "explanation": "La tenencia de saldos monetarios no es forzada. Nadie se queda con billetes ociosos que rinden cero si puede cancelar una deuda con el banco o abrir un depósito a interés."
    },
    {
        "id": "banking_14",
        "question": "¿Qué corriente de la macroeconomía contemporánea reconoce a la Banking School como su principal antecedente doctrinario?",
        "options": [
            "La Escuela de Chicago de Milton Friedman.",
            "La Escuela Poskeynesiana y la Teoría del Circuito Monetario (Monetary Circuit Theory).",
            "La Teoría de las Expectativas Racionales de Robert Lucas.",
            "La Escuela Austríaca de Hayek y Mises."
        ],
        "correct_index": 1,
        "explanation": "Los economistas poskeynesianos contemporáneos (Moore, Kaldor, Lavoie) reivindican a la Banking School por haber descubierto que el dinero es endógeno y creado por el crédito bancario comercial."
    },
    {
        "id": "banking_15",
        "question": "¿Cuál es la diferencia crucial entre un régimen de papel moneda inconvertible (fiduciario forzoso) y los billetes convertibles en el marco de la Banking School?",
        "options": [
            "No existe ninguna diferencia; ambos operan bajo la Ley del Reflujo.",
            "La Ley del Reflujo opera plenamente en billetes convertibles; en papel moneda inconvertible emitido por el Estado para financiar guerras, la sobreemisión permanente sí puede generar inflación.",
            "El papel inconvertible es rechazado universalmente en el comercio.",
            "Los billetes convertibles son destruidos por el banco al final de cada mes."
        ],
        "correct_index": 1,
        "explanation": "Tooke y Fullarton aclararon que su teoría del reflujo aplicaba a billetes comerciales convertibles. Reconocían que si el gobierno emite papel inconvertible forzoso para gasto público, sí puede causar inflación."
    },
    {
        "id": "banking_16",
        "question": "¿Quiénes fueron los tres pensadores más destacados de la Banking School en Gran Bretaña?",
        "options": [
            "David Ricardo, Robert Peel y Lord Overstone.",
            "Thomas Tooke, John Fullarton y James Wilson (fundador de la revista The Economist).",
            "Adam Smith, David Hume y John Stuart Mill.",
            "Irving Fisher, James Tobin y William Baumol."
        ],
        "correct_index": 1,
        "explanation": "Thomas Tooke (autor de History of Prices), John Fullarton (formulador de la Ley del Reflujo) y James Wilson (creador de The Economist en 1843) lideraron la resistencia teórica contra la Ley Peel."
    },
    {
        "id": "banking_17",
        "question": "¿Cómo interpreta la Banking School el papel de los cheques y depósitos en comparación con los billetes físicos?",
        "options": [
            "Como instrumentos peligrosos que debían ser prohibidos por ley.",
            "Como medios de pago de idéntica naturaleza económica que los billetes, que demuestran la imposibilidad de controlar el crédito regulando solo el papel moneda.",
            "Como mercancías de exportación hacia las colonias de la India.",
            "Como activos fijos equivalentes a terrenos y propiedades urbanas."
        ],
        "correct_index": 1,
        "explanation": "La Ley Peel intentó limitar rígidamente los billetes físicos, pero los bancos expandieron el uso de cheques y depósitos en cuenta corriente, eludiendo la restricción y probando la futilidad de controlar solo una forma de liquidez."
    },
    {
        "id": "banking_18",
        "question": "En el debate monetario, ¿cuál es el concepto opuesto al 'Principio de la Moneda' (Currency Principle)?",
        "options": [
            "El Principio Bancario (Banking Principle): la oferta monetaria debe ser elástica y auto-regulada por las necesidades del comercio y la producción.",
            "El Principio Fisiocrático de la fertilidad de la tierra.",
            "El Principio del Multiplicador Keynesiano de importaciones.",
            "El Principio Mercantilista de acumulación de metales preciosos."
        ],
        "correct_index": 0,
        "explanation": "El Principio Bancario sostiene que la emisión de medios de pago debe ser elástica, acompañando los requerimientos de la economía real a través de los mecanismos de intermediación crediticia."
    },
    {
        "id": "banking_19",
        "question": "¿Por qué la Banking School rechazaba que los bancos comerciales pudieran generar inflación especulativa por voluntad propia?",
        "options": [
            "Porque los banqueros estaban supervisados diariamente por inspectores del gobierno.",
            "Porque los bancos comerciales no pueden obligar a los empresarios solventes a endeudarse si estos no observan oportunidades reales de negocios rentables.",
            "Porque los bancos comerciales solo podían operar con comerciantes de su misma familia.",
            "Porque las tasas de interés estaban congeladas por decreto del Rey."
        ],
        "correct_index": 1,
        "explanation": "Para que un banco cree depósitos, debe haber un prestatario dispuesto a asumir una deuda. La iniciativa del crédito parte de la economía real, no del capricho expansivo del banco."
    },
    {
        "id": "banking_20",
        "question": "¿Cuál es la síntesis histórica que reconcilió a la Currency School y la Banking School a fines del siglo XIX bajo Walter Bagehot?",
        "options": [
            "La abolición del patrón oro en todo el mundo.",
            "Se mantuvo la estructura de respaldo de la Ley Peel (Currency) en tiempos normales, pero consagrando la función del Banco Central como Prestamista de Última Instancia elástico (Banking) durante las crisis.",
            "La prohibición de emitir billetes de más de diez chelines.",
            "La privatización total del Departamento de Emisión del Banco de Inglaterra."
        ],
        "correct_index": 1,
        "explanation": "La síntesis de Bagehot (Lombard Street, 1873): disciplina de reservas metálicas en períodos ordinarios (concesión a Currency), combinada con auxilio ilimitado de liquidez ante pánicos (victoria práctica de Banking)."
    }
]

# -------------------------------------------------------------
# 7. RONALD I. MCKINNON (& EDWARD SHAW) (20 preguntas)
# -------------------------------------------------------------
bank_part1["mckinnon"] = [
    {
        "id": "mckinnon_1",
        "question": "¿Cómo define Ronald I. McKinnon el fenómeno de la 'Represión Financiera' en su obra seminal de 1973?",
        "options": [
            "La persecución penal de los banqueros que operan en Wall Street.",
            "El conjunto de políticas estatales que distorsionan y asfixian al sistema financiero doméstico: techos a tasas de interés, encajes no remunerados exorbitantes y crédito dirigido.",
            "La sustitución de la moneda nacional por el dólar estadounidense.",
            "La prohibición de importar maquinarias e insumos para la agricultura."
        ],
        "correct_index": 1,
        "explanation": "McKinnon y Shaw definen la represión financiera como la intervención arbitraria del Estado en el mercado monetario: tasas artificialmente bajas, encajes confiscatorios y racionamiento político del crédito."
    },
    {
        "id": "mckinnon_2",
        "question": "En el marco de McKinnon, ¿cuál es el agregado monetario central acumulado por las familias en países en vías de desarrollo (LDCs)?",
        "options": [
            "M0 (solo monedas divisionarias de bronce).",
            "M2 (circulante y depósitos bancarios a plazo en bancos comerciales).",
            "M3 (incluyendo pagarés bursátiles e hipotecas negociables).",
            "Títulos soberanos de deuda externa de los Estados Unidos."
        ],
        "correct_index": 1,
        "explanation": "Dado que en los países en desarrollo no existen mercados abiertos de bonos o acciones desarrollados, el dinero y los depósitos bancarios a plazo (M2) constituyen casi la totalidad de los activos financieros disponibles."
    },
    {
        "id": "mckinnon_3",
        "question": "¿Qué efecto directo produce la fijación de techos legales a las tasas de interés nominales en contextos de alta inflación?",
        "options": [
            "Estimula una ola sin precedentes de ahorro voluntario en los bancos.",
            "Provoca que la tasa de interés real (r - π) se vuelva fuertemente negativa, castigando al ahorrista y destruyendo los saldos reales M2.",
            "Equilibra instantáneamente la balanza comercial de pagos.",
            "Reduce el déficit presupuestario del gobierno federal a cero."
        ],
        "correct_index": 1,
        "explanation": "Si la inflación es del 40% y el gobierno fija un tope a la tasa pasiva del 15%, la tasa real es -25%. El ahorrista pierde poder adquisitivo mes a mes, huyendo del sistema bancario formal."
    },
    {
        "id": "mckinnon_4",
        "question": "¿Qué ocurre con el ratio de monetización (M2 / PBI) en economías reprimidas frente a países desarrollados?",
        "options": [
            "El ratio M2/PBI supera el 150% en países reprimidos.",
            "El ratio M2/PBI colapsa a niveles raquíticos del 15% al 20%, mientras que en economías con mercados libres ronda el 60% al 80%.",
            "El ratio M2/PBI se mantiene idéntico en todos los países del mundo.",
            "El ratio M2/PBI solo depende del volumen de exportaciones petroleras."
        ],
        "correct_index": 1,
        "explanation": "La represión financiera genera 'desmonetización' o atrofia del sistema financiero: la masa de ahorro formal en los bancos colapsa a una fracción diminuta del producto bruto interno."
    },
    {
        "id": "mckinnon_5",
        "question": "¿Cuál es la función del 'Impuesto Inflacionario' dentro del modelo de represión financiera según McKinnon?",
        "options": [
            "Un subsidio transparente otorgado a los ahorristas rurales.",
            "Un instrumento deliberado del Estado para expropiar recursos del sector privado y financiar el gasto fiscal y la sustitución de importaciones.",
            "Una herramienta para fortalecer la independencia del Banco Central.",
            "Un arancel aplicado exclusivamente a los bienes de lujo importados."
        ],
        "correct_index": 1,
        "explanation": "El Estado utiliza la emisión inflacionaria combinada con encajes forzosos no remunerados para extraer un excedente forzoso de la economía cautiva, subsidiando a sectores urbanos favorecidos."
    },
    {
        "id": "mckinnon_6",
        "question": "¿Cómo se asigna el crédito bancario cuando las tasas de interés están fijadas administrativamente por debajo del equilibrio de mercado?",
        "options": [
            "A través de un remate público transparente al mejor postor.",
            "Mediante racionamiento burocrático y discrecional: los fondos se desvían hacia prestatarios políticamente favorecidos y grandes empresas públicas.",
            "Por estricto orden alfabético de los apellidos de los solicitantes.",
            "Hacia los pequeños campesinos y artesanos del interior del país."
        ],
        "correct_index": 1,
        "explanation": "Con tasas artificialmente bajas, la demanda de crédito excede con creces la oferta de ahorros. Los bancos no eligen proyectos por su productividad o solvencia, sino por cercanía política o colateral previo."
    },
    {
        "id": "mckinnon_7",
        "question": "¿Quiénes son los principales sectores perjudicados por el racionamiento de crédito bajo represión financiera?",
        "options": [
            "Las grandes empresas públicas y los ministerios del gobierno.",
            "Los pequeños productores agrícolas, artesanos y pequeñas y medianas empresas, que quedan marginados hacia prestamistas informales usurarios.",
            "Los bancos transnacionales con sede en Londres.",
            "Los importadores de bienes suntuarios de las grandes capitales."
        ],
        "correct_index": 1,
        "explanation": "El sector rural y las pymes quedan totalmente marginados del crédito bancario formal subsidiado, forzados a endeudarse con prestamistas informales a tasas usurarias o al autofinanciamiento arcaico."
    },
    {
        "id": "mckinnon_8",
        "question": "¿En qué consiste la 'Hipótesis de Complementariedad' formulada por Ronald McKinnon (eje nodal de examen)?",
        "options": [
            "El dinero y el capital físico son activos sustitutos perfectos que compiten en la cartera.",
            "En países en desarrollo, el dinero (M2) y la inversión en capital físico son COMPLEMENTARIOS, no sustitutos.",
            "El crédito bancario debe ser complementado obligatoriamente con préstamos del FMI.",
            "Las exportaciones y las importaciones crecen siempre a la misma tasa porcentual."
        ],
        "correct_index": 1,
        "explanation": "Chocando con la teoría neoclásica de Tobin (donde dinero y capital compiten), McKinnon demuestra que en países subdesarrollados el dinero y la inversión física van de la mano: para invertir en capital, primero hay que acumular dinero."
    },
    {
        "id": "mckinnon_9",
        "question": "¿Por qué el dinero y la inversión en capital físico son complementarios en los países en desarrollo según McKinnon?",
        "options": [
            "Porque los bancos regalan maquinarias a quienes abren cuentas corrientes.",
            "Porque los bienes de capital son costosos e indivisibles, y ante la falta de crédito a largo plazo, el inversor debe ahorrar previamente saldos reales en M2 para comprarlos al contado.",
            "Porque la Constitución de los países emergentes prohíbe el uso de moneda extranjera.",
            "Porque los campesinos solo confían en las monedas de oro acuñadas en el exterior."
        ],
        "correct_index": 1,
        "explanation": "Un tractor o un telar es indivisible y caro. Al no haber crédito de largo plazo para una pyme o un campesino, este debe acumular saldos monetarios en M2 mes tras mes. Si la tasa real es negativa, el ahorro se esfuma y la compra del tractor se vuelve imposible."
    },
    {
        "id": "mckinnon_10",
        "question": "¿Cuál es la 'Trampa del Autofinanciamiento Arcaico' descrita por McKinnon en economías reprimidas?",
        "options": [
            "La obligación legal de pagar los salarios en especie o materias primas.",
            "Al no haber crédito formal, las pequeñas firmas deben financiarse solo con sus propios fondos retenidos, quedando atrapadas en tecnologías obsoletas de baja productividad.",
            "La prohibición de emitir cheques bancarios entre provincias vecinas.",
            "La quiebra obligatoria de las empresas familiares al cabo de cinco años."
        ],
        "correct_index": 1,
        "explanation": "La fragmentación financiera impide canalizar ahorros de unos hacia la inversión productiva de otros. Quien tiene buenas ideas productivas no tiene crédito, y la economía queda estancada en tecnologías primitivas."
    },
    {
        "id": "mckinnon_11",
        "question": "En la función de demanda de dinero de McKinnon (M/P)^d = f(Y, r - π^e, I/Y), ¿qué signo tiene la derivada respecto a la tasa de inversión (I/Y)?",
        "options": [
            "Negativo, porque la inversión destruye la liquidez bancaria.",
            "Positivo (d(M/P)/d(I/Y) > 0), reflejando la complementariedad entre demanda de saldos reales e inversión física.",
            "Cero, porque la inversión es independiente de la moneda.",
            "Indeterminado según las estaciones del año."
        ],
        "correct_index": 1,
        "explanation": "A diferencia del modelo de Tobin (donde d(M/P)/d(I/Y) es negativo porque el capital desplaza al dinero), en McKinnon es POSITIVO: un mayor deseo de invertir exige acumular más saldos monetarios de ahorro."
    },
    {
        "id": "mckinnon_12",
        "question": "¿Qué prescripción fundamental de política económica propone McKinnon para erradicar la represión financiera?",
        "options": [
            "Nacionalizar todas las instituciones de crédito privadas.",
            "La Liberalización Financiera: liberar las tasas de interés para que sean reales positivas (r > π), remunerando al ahorrista y reflejando la verdadera escasez del capital.",
            "Congelar el tipo de cambio nominal a perpetuidad mediante ley marcial.",
            "Fijar encajes obligatorios del 100% sobre todos los depósitos a plazo."
        ],
        "correct_index": 1,
        "explanation": "La receta de McKinnon-Shaw: erradicar los controles administrativos, permitir que las tasas pasivas superen a la inflación para incentivar el ahorro, unificar los mercados de crédito y reducir los encajes bancarios."
    },
    {
        "id": "mckinnon_13",
        "question": "¿Qué concepto define McKinnon como 'Profundización Financiera' (Financial Deepening)?",
        "options": [
            "La construcción de bóvedas subterráneas a gran profundidad.",
            "El crecimiento de los activos financieros y depósitos bancarios a un ritmo superior al del PBI, aumentando la intermediación formal de fondos prestables.",
            "El aumento de la deuda externa soberana con organismos multilaterales.",
            "La emisión de billetes de denominaciones millonarias durante hiperinflaciones."
        ],
        "correct_index": 1,
        "explanation": "Financial Deepening es la expansión del tamaño y la sofisticación del sistema financiero formal respecto a la economía real (suba sostenida del ratio M2/PBI), facilitando la inversión eficiente."
    },
    {
        "id": "mckinnon_14",
        "question": "¿Por qué McKinnon rechaza la doctrina de mantener tasas de interés bajas para incentivar la inversión en países en desarrollo (la 'paradoja keynesiana')?",
        "options": [
            "Porque en países atrasados el cuello de botella no es la falta de incentivos a demandar crédito, sino la escasez física de fondos prestables ahorrados disponibles para prestar.",
            "Porque los bancos prefieren prestar a extranjeros antes que a nacionales.",
            "Porque la tasa de interés baja eleva las exportaciones de petróleo.",
            "Porque la teoría keynesiana fue refutada por David Ricardo en 1810."
        ],
        "correct_index": 0,
        "explanation": "Fijar tasas bajas con la ilusión keynesiana de alentar la inversión destruye el ahorro depositado. Hay miles de proyectos queriendo crédito barato, pero los bancos no tienen fondos que prestar (escasez de oferta de ahorro)."
    },
    {
        "id": "mckinnon_15",
        "question": "¿Qué rol juegan los altos coeficientes de encaje legal bajo represión financiera según McKinnon?",
        "options": [
            "Proteger a los depositantes frente a eventuales fraudes contables.",
            "Operar como un impuesto encubierto no remunerado que confisca los fondos captados por los bancos para financiar el déficit fiscal del gobierno.",
            "Abaratar las tasas de interés de los créditos hipotecarios para familias pobres.",
            "Garantizar la estabilidad de las reservas internacionales en moneda extranjera."
        ],
        "correct_index": 1,
        "explanation": "Los encajes del 50% al 80% congelan los fondos captados en el Banco Central a tasa cero. El gobierno usa esos recursos como crédito fiscal gratuito, asfixiando el crédito productivo al sector privado."
    },
    {
        "id": "mckinnon_16",
        "question": "En el marco de McKinnon y Shaw, ¿cómo afecta la liberalización de tasas de interés a la calidad de los proyectos de inversión financiados?",
        "options": [
            "Empeora la calidad porque solo los proyectos especulativos pueden pagar tasas altas.",
            "Mejora la eficiencia media del capital, ya que solo los proyectos con alta rentabilidad real pueden pagar tasas positivas, expulsando proyectos estatales ineficientes.",
            "Obliga a todas las empresas industriales a cerrar sus plantas de fabricación.",
            "Provoca que todo el capital fluya hacia la compra de tierras ociosas."
        ],
        "correct_index": 1,
        "explanation": "Al costar el capital su verdadero precio de escasez, se termina el subsidio a proyectos estatales improductivos; los fondos se asignan a las actividades privadas que generan mayor valor agregado y productividad."
    },
    {
        "id": "mckinnon_17",
        "question": "¿Qué advertencia posterior formuló McKinnon sobre el 'Orden de la Liberalización Económica' tras las crisis financieras en el Cono Sur en los años 70 y 80?",
        "options": [
            "Que la liberalización financiera debe hacerse en 24 horas sin ningún tipo de control previo.",
            "Que antes de abrir la cuenta de capitales y desregular los bancos, es indispensable lograr el equilibrio fiscal y la estabilización de la inflación interna.",
            "Que los bancos centrales deben fijar el tipo de cambio por debajo del costo de producción.",
            "Que la liberalización financiera es imposible en países con clima tropical."
        ],
        "correct_index": 1,
        "explanation": "En 'The Order of Economic Liberalization' (1991), McKinnon reconoció que liberalizar el crédito sin control bancario ni solvencia fiscal previa desata sobreendeudamiento, quiebras y crisis cambiarias catastróficas."
    },
    {
        "id": "mckinnon_18",
        "question": "¿Qué papel desempeña el 'crédito informal' o paralelo (mercados curb) en economías bajo represión financiera?",
        "options": [
            "Es un mercado minúsculo e irrelevante que no tiene impacto económico.",
            "Es el canal de supervivencia donde los sectores marginados consiguen fondos a tasas exorbitantes debido a la parálisis del sistema bancario formal.",
            "Un programa gubernamental para financiar el cooperativismo rural.",
            "Una red bancaria administrada por el Banco Mundial."
        ],
        "correct_index": 1,
        "explanation": "Ante el estrangulamiento formal, florecen los usureros y circuitos paralelos no supervisados, donde los pequeños productores pagan tasas disparatadas por la falta de un sistema bancario formal desregulado."
    },
    {
        "id": "mckinnon_19",
        "question": "¿Cómo contrasta la hipótesis de McKinnon con la postura del estructuralismo latinoamericano sobre el sector financiero?",
        "options": [
            "McKinnon coincide plenamente en que los controles de tasas son beneficiosos.",
            "Para el estructuralismo las fallas provienen del estrangulamiento externo real, mientras que para McKinnon la atrofia del crédito es una herida autoinfligida por las malas políticas de represión estatal.",
            "Ambas escuelas sostienen que la inflación es siempre y en todo lugar un fenómeno monetario.",
            "El estructuralismo promueve la dolarización y McKinnon la convertibilidad en oro."
        ],
        "correct_index": 1,
        "explanation": "Frente a la justificación estructuralista de cuellos de botella reales, McKinnon demuestra que es el propio Estado el que destruye el mercado crediticio al imponer tasas reales negativas y encajes confiscatorios."
    },
    {
        "id": "mckinnon_20",
        "question": "¿Qué indicador empírico es el termómetro más directo para evaluar el grado de profundización financiera de un país según la literatura de desarrollo?",
        "options": [
            "La cantidad física de billetes de curso legal per cápita.",
            "El ratio M2 / PBI y el nivel de las tasas de interés reales pasivas.",
            "El número de bancos extranjeros instalados en la capital del país.",
            "La cotización de las acciones de empresas mineras en Wall Street."
        ],
        "correct_index": 1,
        "explanation": "Un ratio M2/PBI elevado y tasas de interés reales moderadamente positivas reflejan la confianza del público en el sistema financiero doméstico y una sólida canalización del ahorro voluntario hacia la inversión."
    }
]

# -------------------------------------------------------------
# 8. JULIO H. G. OLIVERA Y ALFREDO CANAVESE (20 preguntas)
# -------------------------------------------------------------
bank_part1["olivera_canavese"] = [
    {
        "id": "olivera_1",
        "question": "¿Cuál es la premisa originaria de la Escuela Estructuralista latinoamericana sobre la causa de la inflación?",
        "options": [
            "La inflación es siempre un fenómeno generado por la sobreemisión arbitraria de billetes de banco.",
            "La inflación no es un fenómeno originariamente monetario, sino el resultado de estrangulamientos y rigideces en la estructura productiva real combinados con rigideces de precios a la baja.",
            "La inflación proviene de las tasas de interés excesivamente altas fijadas por bancos transnacionales.",
            "La inflación es provocada exclusivamente por los gastos electorales de los partidos políticos."
        ],
        "correct_index": 1,
        "explanation": "Para la CEPAL y Olivera, la causa motriz reside en cuellos de botella estructurales de oferta (sector agrario y externo) que exigen cambios en precios relativos en una economía donde nada baja de precio nominal."
    },
    {
        "id": "olivera_2",
        "question": "¿En qué consiste el 'Estrangulamiento Agrícola' según el diagnóstico estructuralista de la inflación?",
        "options": [
            "En la caída del consumo de carne debido a cambios culturales vegetarianos.",
            "En la inelasticidad de la oferta de alimentos frente al aumento de la demanda urbana, derivada del régimen de tenencia de la tierra y la falta de inversión, lo que dispara los precios agrícolas.",
            "En la invasión de plagas que destruyen las cosechas cada dos años.",
            "En la fijación de precios máximos que arruina a los supermercados."
        ],
        "correct_index": 1,
        "explanation": "Con la urbanización e industrialización, la demanda de alimentos crece velozmente. Al ser la producción agrícola estructuralmente inelástica, el precio relativo de los alimentos debe subir sustancialmente."
    },
    {
        "id": "olivera_3",
        "question": "¿En qué consiste el 'Estrangulamiento Externo' analizado por el estructuralismo (tesis Prebisch-Singer)?",
        "options": [
            "En el cierre militar de los puertos marítimos internacionales.",
            "En la escasez crónica de divisas provocada por el deterioro de los términos de intercambio y la baja elasticidad-ingreso de las exportaciones primarias frente a las manufacturas importadas.",
            "En la negativa de los países vecinos a utilizar la misma moneda regional.",
            "En el cobro de aranceles cero a los productos extranjeros."
        ],
        "correct_index": 1,
        "explanation": "La tendencia al deterioro de los términos de intercambio y la necesidad de insumos industriales importados genera crisis periódicas de balanza de pagos, forzando devaluaciones que encarecen insumos y alimentos."
    },
    {
        "id": "olivera_4",
        "question": "¿Qué papel juega el supuesto de 'Inflexibilidad a la Baja' de precios y salarios en la teoría estructuralista?",
        "options": [
            "Garantiza que la economía retorne instantáneamente al pleno empleo walrasiano.",
            "Dado que los precios relativos deben cambiar por los estrangulamientos y los sectores sin problemas no bajan sus precios nominales, el ajuste solo puede darse elevando el nivel general de precios.",
            "Impide que el gobierno cobre impuestos sobre las exportaciones agropecuarias.",
            "Asegura que las tasas de interés se mantengan negativas en términos reales."
        ],
        "correct_index": 1,
        "explanation": "Si el precio relativo de los alimentos debe subir respecto a los bienes industriales, pero los precios industriales no bajan por márgenes oligopólicos, la única forma matemática de ajustar la relación es subiendo todos los precios."
    },
    {
        "id": "olivera_5",
        "question": "¿En qué consiste el célebre 'Teorema de la Oferta Monetaria Pasiva' formulado por Julio H. G. Olivera (1957/1960)?",
        "options": [
            "En que el Banco Central debe cerrar sus ventanillas los días viernes.",
            "En que la cantidad de dinero no es la causa originaria de la inflación, sino una variable pasiva y convalidante que el Banco Central debe expandir para evitar quiebras e iliquidez.",
            "En que la emisión monetaria siempre genera pleno empleo sin inflación.",
            "En que los depósitos bancarios no devengan intereses en economías periféricas."
        ],
        "correct_index": 1,
        "explanation": "Aporte central de Olivera: la oferta monetaria es endógena y pasiva. La inflación empuja a la emisión, y no al revés, porque si el Banco Central congelara el dinero causaría una depresión productiva."
    },
    {
        "id": "olivera_6",
        "question": "¿Qué es la 'Brecha Deflacionaria' descrita por Olivera si la autoridad monetaria se niega a emitir dinero pasivo?",
        "options": [
            "Una reducción en los costos de transporte marítimo de mercancías.",
            "Una contracción violenta de los saldos reales (M/P cae) que genera iliquidez generalizada, acumulación de inventarios invendibles, quiebras masivas de empresas solventes y desempleo.",
            "Un aumento extraordinario de las reservas de divisas en el Banco Central.",
            "Una disminución de los precios agrícolas por debajo de los costos de siembra."
        ],
        "correct_index": 1,
        "explanation": "Al subir los precios por shocks de oferta, si M se mantiene congelada, M/P se derrumba. La falta de liquidez paraliza el circuito de pagos y provoca quiebras masivas de firmas viables."
    },
    {
        "id": "olivera_7",
        "question": "¿Por qué el Banco Central se ve 'forzado institucionalmente' a convalidar la inflación según Olivera?",
        "options": [
            "Porque la ley le prohíbe tener superávit operativo en sus balances anuales.",
            "Porque entre convalidar monetariamente el shock de precios o permitir el colapso productivo y la quiebra del sistema bancario, la autoridad opta racionalmente por emitir.",
            "Porque los gobernadores del Banco Central reciben comisiones por cada billete emitido.",
            "Porque los sindicatos toman las instalaciones del Banco Central durante las devaluaciones."
        ],
        "correct_index": 1,
        "explanation": "La autoridad monetaria enfrenta un dilema asimétrico: convalidar la suba de precios con dinero pasivo o desencadenar una recesión catastrófica. La emisión es una adaptación forzosa del sistema financiero a la realidad estructural."
    },
    {
        "id": "olivera_8",
        "question": "¿Qué demostración matemática crucial realizó Alfredo Canavese en su clásico ensayo de 1979 ('La hipótesis estructural en la teoría de la inflación')?",
        "options": [
            "Demostró que la curva de Phillips es horizontal en todos los países del Tercer Mundo.",
            "Probó la estricta equivalencia formal entre el modelo estructuralista latinoamericano y los modelos anglosajones de traslación de demanda (Schultze) y productividad (Baumol).",
            "Demostró que el señoreaje fiscal es matemáticamente idéntico a la recaudación aduanera.",
            "Refutó el teorema de Pitágoras aplicado a series de tiempo financieras."
        ],
        "correct_index": 1,
        "explanation": "Canavese otorga respetabilidad analítica universal al estructuralismo al demostrar que los modelos cepalinos (Noyola, Sunkel, Olivera) son formalmente equivalentes al modelo de demand-shift inflation de Charles Schultze (EE.UU.) y Baumol."
    },
    {
        "id": "olivera_9",
        "question": "En el modelo de Charles Schultze (1959) analizado por Canavese, ¿cómo genera inflación una simple traslación de demanda sin exceso de demanda agregada global?",
        "options": [
            "Por el aumento del gasto militar en armamento pesado.",
            "La demanda se traslada del sector A al sector B: en B los precios suben por exceso de demanda, pero en A no bajan debido a precios rígidos; el promedio general de precios se eleva.",
            "Por el colapso súbito del sistema de pagos interbancario de la Reserva Federal.",
            "Por la quiebra simultánea de los productores agropecuarios de granos."
        ],
        "correct_index": 1,
        "explanation": "Schultze probó que con demanda global constante, si la composición de la demanda cambia entre sectores y existe asimetría de precios (flexibles al alza, rígidos a la baja), el nivel general de precios sube obligatoriamente."
    },
    {
        "id": "olivera_10",
        "question": "En el modelo de William Baumol (1967) y el modelo escandinavo estudiado por Canavese, ¿cómo se traslada la inflación entre sectores?",
        "options": [
            "A través de subsidios directos pagados por el parlamento a las industrias textiles.",
            "El sector dinámico de alta productividad aumenta salarios reales; el sector estancado de servicios debe igualar esos salarios para no perder personal, pero al no tener productividad traslada el costo a precios.",
            "Mediante la devaluación forzosa de la moneda en los mercados cambiarios libres.",
            "A través del cobro de tarifas de peaje en las autopistas interurbanas."
        ],
        "correct_index": 1,
        "explanation": "La 'enfermedad de costos' de Baumol: los salarios tienden a igualarse entre sectores; las actividades con baja productividad ven dispararse sus costos laborales unitarios y elevan sus precios."
    },
    {
        "id": "olivera_11",
        "question": "¿Cómo clasifica la literatura estructuralista los componentes del proceso inflacionario?",
        "options": [
            "En inflación buena, inflación regular e inflación mala.",
            "En presiones básicas o estructurales, mecanismos de propagación (puja distributiva) y factores convalidantes (emisión monetaria y déficit fiscal).",
            "En inflación trimestral, inflación semestral e inflación anualizada.",
            "En factores dependientes del dólar y factores dependientes del oro."
        ],
        "correct_index": 1,
        "explanation": "Clasificación canónica de Osvaldo Sunkel: 1) Presiones básicas (estrangulamientos reales); 2) Mecanismos de propagación (espiral salarios-precios); 3) Factores convalidantes (política fiscal y monetaria pasiva)."
    },
    {
        "id": "olivera_12",
        "question": "¿Por qué los programas de estabilización ortodoxos del FMI basados en contracción monetaria fracasan según el diagnóstico estructuralista?",
        "options": [
            "Porque los funcionarios del FMI no dominan el idioma español.",
            "Porque intentar frenar los precios contrayendo el crédito no elimina los estrangulamientos reales de alimentos ni de divisas, pero paraliza la producción generando estanflación severa.",
            "Porque la contracción monetaria reduce automáticamente las tasas de interés bancarias.",
            "Porque los bancos comerciales aumentan sus préstamos cuando el Banco Central restringe la base."
        ],
        "correct_index": 1,
        "explanation": "La receta ortodoxa ataca el síntoma monetario pero no la causa real. Al cortar el crédito en una economía con cuellos de botella, las firmas quiebran y el PBI cae en picada sin resolver la inelasticidad de la oferta agrícola ni la escasez de dólares."
    },
    {
        "id": "olivera_13",
        "question": "¿Cuál es la prescripción de política económica central que propone el estructuralismo para erradicar la inflación de forma duradera?",
        "options": [
            "Dolarizar de inmediato la economía y cerrar el Banco Central.",
            "Políticas de desarrollo y reformas estructurales: tecnificación agrícola, diversificación de exportaciones e inversión en infraestructura para superar estrangulamientos.",
            "Fijar encajes del 100% sobre todos los depósitos a la vista.",
            "Reducir los salarios reales de los trabajadores industriales un 50% por decreto."
        ],
        "correct_index": 1,
        "explanation": "La única solución permanente es la transformación estructural: reforma agraria/tecnificación para que la oferta de alimentos sea elástica y sustitución/diversificación exportadora para levantar la restricción de divisas."
    },
    {
        "id": "olivera_14",
        "question": "¿En qué consiste el 'Efecto Olivera-Tanzi' ampliamente reconocido en la literatura de finanzas públicas?",
        "options": [
            "En el aumento extraordinario de las reservas de divisas durante los planes de convertibilidad.",
            "En el deterioro y caída de la recaudación tributaria real provocado por los rezagos de cobranza impositiva en contextos de aceleración inflacionaria.",
            "En la sustitución del impuesto a las ganancias por retenciones agropecuarias.",
            "En la fijación de tasas de interés pasivas negativas por parte de los bancos comerciales."
        ],
        "correct_index": 1,
        "explanation": "Formulado por Olivera (1967) y Tanzi (1977): entre el momento en que se genera la obligación tributaria y el día en que el Estado efectivamente recauda el impuesto transcurre un lapso; si la inflación es alta, el valor real recaudado se pulveriza."
    },
    {
        "id": "olivera_15",
        "question": "¿Cómo interactúa el Efecto Olivera-Tanzi con el déficit fiscal y la emisión monetaria?",
        "options": [
            "Genera un círculo virtuoso que equilibra el presupuesto público de forma automática.",
            "Genera una espiral destructiva: la inflación deprime la recaudación real $\\rightarrow$ el déficit fiscal se agranda $\\rightarrow$ el gobierno emite más dinero pasivo $\\rightarrow$ la inflación se acelera más.",
            "Permite al Estado cancelar su deuda externa soberana con fondos propios.",
            "Reduce la necesidad de cobrar impuestos sobre las ventas minoristas."
        ],
        "correct_index": 1,
        "explanation": "Espiral viciosa: al derrumbarse los ingresos fiscales reales por rezagos de cobranza, el bache fiscal se ensancha, obligando a emitir más dinero para cubrir el gasto corriente, retroalimentando la inflación."
    },
    {
        "id": "olivera_16",
        "question": "En el análisis estructuralista, ¿cuál es el papel de la 'Puja Distributiva' en la dinámica inflacionaria?",
        "options": [
            "Es un fenómeno pacífico que se resuelve mediante arbitraje judicial en tribunales internacionales.",
            "Es el mecanismo de propagación mediante el cual asalariados y empresarios intentan trasladarse mutuamente el costo de los shocks de precios relativos a través de salarios nominales y márgenes de ganancia.",
            "Una competencia deportiva organizada anualmente por los sindicatos fabriles.",
            "La negociación de aranceles de importación entre países miembros de la CEPAL."
        ],
        "correct_index": 1,
        "explanation": "La puja distributiva es el engranaje que perpetúa el alza de precios: ante el shock de alimentos o devaluación, los trabajadores exigen recomponer el salario real; las empresas aumentan precios para defender sus márgenes, propagando la inflación."
    },
    {
        "id": "olivera_17",
        "question": "¿Qué crítica metodológica formula el estructuralismo a los modelos neoclásicos de equilibrio general walrasiano?",
        "options": [
            "Que no utilizan el idioma español en sus demostraciones algebraicas.",
            "Que asumen mercados perfectamente homogéneos, competitivos y sin fricciones, ignorando la heterogeneidad productiva, los monopolios y las asimetrías de poder de las economías periféricas.",
            "Que los modelos walrasianos exigen la abolición del Banco Central.",
            "Que no consideran la existencia del tipo de cambio fijo."
        ],
        "correct_index": 1,
        "explanation": "El estructuralismo rechaza la ficción de mercados perfectos y vaciado continuo: América Latina se caracteriza por dualismo productivo, oligopolios formadores de precios y mercados segmentados que invalidan los supuestos neoclásicos."
    },
    {
        "id": "olivera_18",
        "question": "¿Por qué Olivera distingue entre la 'inflación no monetaria' y la convalidación monetaria de los precios?",
        "options": [
            "Porque la inflación no monetaria se mide en dólares y la convalidación en moneda nacional.",
            "Para enfatizar que la causa generadora es real y no monetaria, pero que sin la convalidación cuantitativa del medio de pago el sistema caería en colapso por falta de liquidez.",
            "Porque la convalidación solo ocurre durante los fines de semana largos.",
            "Para eximir de toda responsabilidad penal a los directores del Banco Central."
        ],
        "correct_index": 1,
        "explanation": "Distinción crucial para examen: la causa originaria de la suba de precios es estructural; el dinero entra como factor permisivo y convalidante necesario para que el sistema productivo no se paralice."
    },
    {
        "id": "olivera_19",
        "question": "¿Qué vinculación existe entre el modelo de Canavese (1979) y el régimen de inflación escandinavo de Aukrust?",
        "options": [
            "Canavese demuestra que en ambos modelos la inflación es exportada por los países petroleros de Medio Oriente.",
            "Ambos modelos dividen la economía en un sector expuesto a la competencia internacional (precios fijados afuera) y un sector protegido no transable (precios guiados por costos salariales).",
            "Ambos modelos postulan el retorno obligatorio al patrón oro internacional.",
            "Canavese utilizó exclusivamente datos trimestrales de la economía de Suecia y Noruega."
        ],
        "correct_index": 1,
        "explanation": "En el modelo escandinavo, los salarios del sector protegido siguen a los del sector transable; al tener menor productividad, el sector protegido traslada el costo a precios, generando una inflación estructural idéntica a la descrita por Canavese."
    },
    {
        "id": "olivera_20",
        "question": "¿Cuál es la conclusión de Canavese sobre la política antiinflacionaria en economías estructuralmente heterogéneas?",
        "options": [
            "Que la política monetaria contractiva pura es el remedio más eficiente y equitativo.",
            "Que la desinflación no puede alcanzarse solo con instrumentos monetarios sin un costo catastrófico en desempleo y quiebras, requiriendo acuerdos de ingresos, política cambiaria y reformas sectoriales de oferta.",
            "Que la inflación desaparece por sí sola al cabo de tres trimestres de libre competencia.",
            "Que el Estado debe subsidiar en un 100% el consumo de bienes importados."
        ],
        "correct_index": 1,
        "explanation": "Al provenir de rigideces estructurales y pujas distributivas, frenar la inflación solo con torniquete monetario genera recesión devastadora. Se requiere una estrategia integral: política de ingresos, coordinación de precios y resolución de cuellos de botella reales."
    }
]

print(f"Cargadas las 100 preguntas de la Parte 1 (Bernanke, Currency, Banking, McKinnon, Olivera).")

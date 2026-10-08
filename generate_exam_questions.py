# -*- coding: utf-8 -*-
"""
generate_exam_questions.py
Generates the comprehensive university exam question bank:
20 theoretical multiple-choice questions per economist/school across all 13 syllabus subjects (260 questions total).
"""

import json
import os

questions_bank = {}

# 1. MILTON FRIEDMAN
questions_bank["friedman"] = [
    {
        "id": "friedman_1",
        "question": "¿Cuál es el criterio metodológico fundamental que adopta Milton Friedman para definir el concepto empírico adecuado de dinero?",
        "options": [
            "Un criterio ontológico basado en las propiedades físicas de durabilidad y divisibilidad del metal precioso.",
            "Un criterio instrumental y pragmático: el agregado cuya relación estadística con el ingreso nominal resulte más estable y predictiva.",
            "La doctrina jurídica que reconoce únicamente como dinero a las monedas de curso legal forzoso emitidas por el Estado.",
            "La definición de dinero como el conjunto infinito de activos líquidos que rinden servicios de pago según el Informe Radcliffe."
        ],
        "correct_index": 1,
        "explanation": "En su metodología positiva (1953) e investigaciones empíricas (1970), Friedman adopta un criterio estrictamente instrumental: el dinero adecuado es aquel agregado estadístico que guarde la relación más estable y predictiva con el ingreso nacional nominal."
    },
    {
        "id": "friedman_2",
        "question": "¿Por qué Milton Friedman y Anna Schwartz seleccionan M2 en lugar de M1 como su agregado monetario de referencia?",
        "options": [
            "Porque M1 incluía oro físico que ya no circulaba en los Estados Unidos.",
            "Porque consideran que los depósitos a plazo en bancos comerciales son sustitutos casi perfectos de los depósitos a la vista.",
            "Porque la Reserva Federal no tenía capacidad legal para medir la base monetaria en M1.",
            "Porque los depósitos a plazo no devengan tasa de interés en el sistema financiero estadounidense."
        ],
        "correct_index": 1,
        "explanation": "Friedman y Schwartz demuestran empíricamente que los depósitos a plazo en bancos comerciales satisfacen la misma demanda de saldos de reserva del público que las cuentas corrientes, haciendo que M2 sea el agregado más estable."
    },
    {
        "id": "friedman_3",
        "question": "En la 'Reformulación de la Teoría Cuantitativa' (1956), ¿cómo define Friedman la naturaleza de la teoría cuantitativa?",
        "options": [
            "Como una teoría acabada del nivel general de precios y del tipo de cambio.",
            "Como una teoría estricta de la producción real y el pleno empleo.",
            "Estrictamente como una teoría de la demanda de dinero, no del producto ni de los precios.",
            "Como una derivación matemática directa de la ecuación de balance de la Banking School."
        ],
        "correct_index": 2,
        "explanation": "Friedman postula taxativamente: 'la teoría cuantitativa es en primer lugar una teoría de la demanda de dinero. No es una teoría de la producción que se obtendría o del ingreso monetario o del nivel de precios'."
    },
    {
        "id": "friedman_4",
        "question": "¿Qué variable utiliza Milton Friedman como la restricción presupuestaria básica en su función de demanda de dinero?",
        "options": [
            "El ingreso corriente trimestral medido por las cuentas nacionales.",
            "El volumen físico de transacciones comerciales T de Fisher.",
            "La riqueza total de los individuos, aproximada a través del Ingreso Permanente (Yp).",
            "El saldo de reservas excedentes depositadas en el Banco Central."
        ],
        "correct_index": 2,
        "explanation": "Friedman rechaza el ingreso corriente keynesiano y utiliza la riqueza total, operacionalizada mediante el Ingreso Permanente (Yp), entendido como el flujo constante descontado de los ingresos que un agente espera recibir a lo largo de su vida."
    },
    {
        "id": "friedman_5",
        "question": "¿Qué representa la variable 'w' en la función de demanda de saldos monetarios reales de Friedman (M/P)^d = f(Yp, w, ...)?",
        "options": [
            "El nivel general de salarios nominales negociados por convenios colectivos.",
            "La proporción de riqueza humana (capacidad de generar trabajo futuro) respecto a la riqueza no humana.",
            "El coeficiente de ponderación de las importaciones en la canasta de consumo.",
            "La velocidad de circulación del dinero en el corto plazo."
        ],
        "correct_index": 1,
        "explanation": "La variable 'w' es la fracción de riqueza humana respecto a la no humana. Al ser la riqueza humana ilíquida (no se puede enajenar en un mercado secundario), a mayor 'w' mayor necesidad de retener saldos monetarios líquidos de reserva."
    },
    {
        "id": "friedman_6",
        "question": "¿Qué postula Friedman acerca de la estabilidad de la función de demanda de dinero?",
        "options": [
            "Que la velocidad de circulación es una constante matemática fija e inmutable.",
            "Que la demanda de dinero es sumamente errática debido a los espíritus animales de los inversores.",
            "Que la función es notablemente estable en el tiempo y depende de pocas variables observables de riqueza y rendimientos relativos.",
            "Que colapsa permanentemente en trampas de liquidez keynesianas."
        ],
        "correct_index": 2,
        "explanation": "La velocidad V no es fija, pero la función de demanda de dinero es notablemente estable. Por ende, las variaciones no explicadas del ingreso nominal provienen de perturbaciones en la oferta monetaria generadas por el Banco Central."
    },
    {
        "id": "friedman_7",
        "question": "Según el monetarismo, ¿cuál es el mecanismo exacto de transmisión mediante el cual un aumento en la oferta monetaria genera inflación?",
        "options": [
            "Aumenta la tasa de interés de los bonos, encareciendo los créditos productivos.",
            "Genera un exceso de saldos reales (M/P > deseado) que el público gasta en bienes y activos, presionando los precios al alza.",
            "Reduce los costos marginales de producción, forzando a los sindicatos a reclamar salarios más altos.",
            "Produce una devaluación del tipo de cambio fijo por agotamiento automático de las reservas de oro."
        ],
        "correct_index": 1,
        "explanation": "Al inyectarse dinero, el público se encuentra con saldos reales mayores a los deseados según su función estable. Intentan deshacerse del excedente comprando bienes y activos, empujando la demanda agregada y los precios al alza hasta restaurar el equilibrio."
    },
    {
        "id": "friedman_8",
        "question": "¿Cuál es la famosa máxima de Friedman sobre la causa última de la inflación sostenida?",
        "options": [
            "La inflación es siempre el resultado inevitable de la puja distributiva de los sindicatos.",
            "La inflación es siempre y en todo lugar un fenómeno monetario.",
            "La inflación es la consecuencia exclusiva del estrangulamiento de la balanza de pagos.",
            "La inflación es un fenómeno psicológico generado por la incertidumbre radical del futuro."
        ],
        "correct_index": 1,
        "explanation": "Friedman sentencia: 'La inflación es siempre y en todo lugar un fenómeno monetario, en el sentido de que solo es y puede ser producida por un aumento de la cantidad de dinero más rápido que el de la producción'."
    },
    {
        "id": "friedman_9",
        "question": "¿Cómo refuta Friedman la teoría de que los sindicatos o las subas del petróleo causan inflación sostenida?",
        "options": [
            "Afirma que los sindicatos carecen de poder monopólico en las economías occidentales.",
            "Demuestra que solo generan un cambio transitorio de precios relativos de una sola vez, salvo que el Banco Central convalide emitiendo dinero.",
            "Sostiene que el precio del petróleo baja automáticamente por mecanismos de mercado en menos de un mes.",
            "Argumenta que los empresarios nunca trasladan aumentos de costos a los precios finales de venta."
        ],
        "correct_index": 1,
        "explanation": "Los shocks sectoriales o reclamos salariales modifican precios relativos. Si la masa de dinero no crece, otros precios caen o sube el desempleo; solo hay inflación persistente si la autoridad monetaria emite para convalidar el shock."
    },
    {
        "id": "friedman_10",
        "question": "En el modelo monetarista, ¿cómo se relaciona la oferta monetaria total (M) con la base monetaria (B)?",
        "options": [
            "M = B / (c + r), donde el crédito no juega ningún papel intermediador.",
            "M = m · B, donde el multiplicador m = (c + 1) / (c + r), siendo c la preferencia por efectivo y r el encaje bancario.",
            "M = B · (1 - r), donde el público no mantiene efectivo físico en su poder.",
            "M es completamente independiente de B y depende exclusivamente de la demanda de crédito comercial."
        ],
        "correct_index": 1,
        "explanation": "M es el producto de la base monetaria B por el multiplicador m = (c+1)/(c+r). Aunque c y r fluctúan en el corto plazo, el Banco Central dispone de instrumentos para neutralizar las desviaciones y gobernar la cantidad de dinero final."
    },
    {
        "id": "friedman_11",
        "question": "En 'A Monetary History of the United States' (1963), ¿cuál fue la causa principal de la Gran Depresión de 1929 según Friedman y Schwartz?",
        "options": [
            "El colapso inherente de la inversión privada provocado por la irracionalidad del capitalismo.",
            "La contracción de un tercio (-33%) de la oferta de dinero permitida por la nefasta gestión de la Reserva Federal.",
            "La imposición de encajes del 100% que paralizó a los bancos de inversión de Wall Street.",
            "El financiamiento excesivo de obras públicas con déficit presupuestario keynesiano."
        ],
        "correct_index": 1,
        "explanation": "Friedman y Schwartz demuestran que la Gran Depresión no fue una falla del libre mercado, sino una catástrofe provocada por la Fed al permitir que la masa monetaria cayera un tercio sin actuar como prestamista de última instancia ante los pánicos bancarios."
    },
    {
        "id": "friedman_12",
        "question": "¿Por qué Friedman sostiene que la Curva de Phillips es vertical en el largo plazo?",
        "options": [
            "Porque los trabajadores sufren de ilusión monetaria permanente e irreversible.",
            "Porque los agentes corrigen sus expectativas adaptativas de inflación, retornando el desempleo a su Tasa Natural (u_n).",
            "Porque el gobierno fija los salarios mediante decretos congelados por ley.",
            "Porque la productividad del trabajo se vuelve infinitamente inelástica ante la tasa de interés."
        ],
        "correct_index": 1,
        "explanation": "A corto plazo, una emisión imprevista engaña transitoriamente a los trabajadores. A largo plazo corrigen sus expectativas adaptativas de inflación y reclaman subas salariales; el desempleo retorna a la tasa natural un y la curva se vuelve vertical."
    },
    {
        "id": "friedman_13",
        "question": "¿En qué consiste la prescripción de política conocida como la 'Regla del k%' de Milton Friedman?",
        "options": [
            "Aumentar la tasa de interés de política monetaria en k puntos porcentuales cada vez que el desempleo suba.",
            "Incrementar la oferta monetaria a una tasa fija y constante anual (3% al 5%) alineada con el crecimiento del producto potencial.",
            "Permitir al Banco Central la máxima discrecionalidad anticíclica mensual.",
            "Fijar el coeficiente de encaje bancario obligatorio en exactamente k% para todos los depósitos."
        ],
        "correct_index": 1,
        "explanation": "Debido a los rezagos temporales, Friedman aconseja erradicar la discrecionalidad de los bancos centrales y someterlos a una regla estricta: expandir la masa monetaria a un ritmo constante (entre el 3% y el 5% anual) coherente con el crecimiento del PBI real."
    },
    {
        "id": "friedman_14",
        "question": "¿Qué argumento central esgrime Friedman en contra de las políticas de sintonía fina ('fine-tuning') keynesianas?",
        "options": [
            "Que el multiplicador del gasto fiscal es matemáticamente infinito.",
            "La existencia de rezagos temporales largos y variables (lags) que vuelven procíclicas a las intervenciones discrecionales.",
            "Que los bancos comerciales se niegan a otorgar préstamos durante los períodos electorales.",
            "Que el gasto público reduce instantáneamente el nivel general de precios al generar competencia."
        ],
        "correct_index": 1,
        "explanation": "Los retardos de reconocimiento, decisión y acción operan con efectos retrasados impredecibles. Cuando la inyección expansiva llega a la economía, esta ya se encuentra en fase de auge, sobrecalentando el ciclo."
    },
    {
        "id": "friedman_15",
        "question": "En 'La Metodología de la Economía Positiva' (1953), ¿qué sostiene Friedman respecto al realismo de los supuestos de una teoría?",
        "options": [
            "Que una teoría solo es científicamente válida si sus premisas describen fotográficamente la realidad cotidiana.",
            "Que la validez de una teoría debe juzgarse por la precisión de sus predicciones empíricas y no por el realismo descriptivo de sus supuestos.",
            "Que los supuestos deben ser aprobados previamente mediante encuestas sociológicas a empresarios.",
            "Que cualquier abstracción matemática invalida la coherencia de una teoría económica positiva."
        ],
        "correct_index": 1,
        "explanation": "El núcleo del instrumentalismo: una teoría relevante no busca reproducir la realidad en sus supuestos, sino explicar mucho con poco. Cuanto más significativa es la teoría, más abstractos e irreales suelen ser sus supuestos."
    },
    {
        "id": "friedman_16",
        "question": "¿En qué consiste el principio metodológico del 'como si' (as if) propuesto por Friedman?",
        "options": [
            "En suponer que los consumidores actúan con desinterés y altruismo en el mercado de bienes.",
            "En postular que los agentes se comportan 'como si' optimizaran complejas funciones matemáticas, aunque no las calculen conscientemente.",
            "En afirmar que el dinero opera como si no existieran bancos comerciales en la economía.",
            "En diseñar políticas públicas como si el Banco Central fuera un organismo dependiente del Poder Judicial."
        ],
        "correct_index": 1,
        "explanation": "Al igual que un jugador experto de billar tira 'como si' conociera las ecuaciones cinemáticas, los agentes económicos se comportan 'como si' maximizaran retornos intertemporales, haciendo válidas las predicciones del modelo."
    },
    {
        "id": "friedman_17",
        "question": "¿Cómo se forman las expectativas sobre la inflación futura en el modelo clásico de Friedman?",
        "options": [
            "Bajo previsión perfecta instantánea de todos los eventos del futuro.",
            "Mediante expectativas adaptativas, ponderando los errores pasados de predicción a lo largo del tiempo.",
            "A través de encuestas psicológicas publicadas en los periódicos matutinos.",
            "Bajo expectativas racionales donde los errores de pronóstico son exclusivamente ruido blanco ortogonal."
        ],
        "correct_index": 1,
        "explanation": "Friedman formula expectativas adaptativas: los individuos revisan gradualmente su tasa esperada de inflación a medida que experimentan errores en los períodos anteriores (mecanismo retrospectivo)."
    },
    {
        "id": "friedman_18",
        "question": "¿Qué postura asume Milton Friedman frente a las regulaciones de tasas de interés y controles de crédito estatal?",
        "options": [
            "Defiende los techos a las tasas de interés para promover el crédito barato a las industrias nacientes.",
            "Condena los controles de precios y tasas, sosteniendo que distorsionan la asignación del capital y castigan el ahorro voluntario.",
            "Propone que el Estado fije márgenes de intermediación bancaria garantizados por ley.",
            "Considera irrelevante la tasa de interés debido a la perfecta sustituibilidad del dinero físico."
        ],
        "correct_index": 1,
        "explanation": "Friedman condena enérgicamente los techos legales a tasas de interés pasivas y activas, señalando que provocan escasez de crédito genuino y distorsionan la eficiencia productiva, inspirando a la escuela de desarrollo financiero."
    },
    {
        "id": "friedman_19",
        "question": "En el debate sobre la definición del dinero, ¿contra qué dos extremos se posiciona la síntesis monetarista de Friedman?",
        "options": [
            "Contra el mercantilismo del siglo XVI y la fisiocracia francesa.",
            "Contra la extrema estrechez de la Currency School (solo metal/billetes) y la extrema laxitud del Informe Radcliffe (liquidez general difusa).",
            "Contra la Escuela Austríaca y la Escuela Neoclásica de Walras.",
            "Contra los modelos de equilibrio general dinámico y la teoría de juegos cooperativos."
        ],
        "correct_index": 1,
        "explanation": "Friedman demuestra que M2 evita la trampa de considerar únicamente el circulante metálico o de diluir el concepto de dinero en un mar de sustitutos de crédito incontrolables como proponía Radcliffe."
    },
    {
        "id": "friedman_20",
        "question": "¿Qué ocurre con la demanda de saldos reales de Friedman si se incrementa la tasa esperada de inflación (π^e)?",
        "options": [
            "Aumenta exponencialmente porque el público busca atesorar más billetes para pagar precios altos.",
            "Permanece inalterada porque el dinero rinde un flujo constante de servicios de transacción.",
            "Disminuye, ya que la inflación actúa como un costo de oportunidad de mantener dinero frente a activos reales.",
            "Se vuelve infinitamente elástica cayendo en una trampa de liquidez."
        ],
        "correct_index": 2,
        "explanation": "La inflación esperada mide la tasa de depreciación del dinero frente a los bienes físicos. Al elevarse π^e, el costo de mantener saldos monetarios sube y la demanda real (M/P)^d cae."
    }
]

# 2. JOHN MAYNARD KEYNES
questions_bank["keynes"] = [
    {
        "id": "keynes_1",
        "question": "En la 'Teoría General' (1936), ¿cuál es la propiedad esencial que distingue al dinero de los demás activos?",
        "options": [
            "Su costo marginal de producción físico y su respaldo directo en reservas metálicas.",
            "Su liquidez: la capacidad inmediata de cancelar deudas y actuar como eslabón institucional hacia un futuro incierto.",
            "Que devenga una tasa fija de interés garantizada por el Tesoro.",
            "Que su valor de cambio está determinado exclusivamente por el tiempo de trabajo incorporado."
        ],
        "correct_index": 1,
        "explanation": "Keynes define al dinero como el activo líquido por excelencia, cuyo valor fundamental reside en otorgar seguridad y posponer decisiones irreversibles en un entorno dominado por la incertidumbre del futuro."
    },
    {
        "id": "keynes_2",
        "question": "¿Cuáles son los tres motivos diferenciados de demanda de dinero formulados por Keynes en su teoría de la Preferencia por la Liquidez?",
        "options": [
            "Motivo Consumo, Motivo Producción y Motivo Ahorro.",
            "Motivo Transacción, Motivo Precaución y Motivo Especulación.",
            "Motivo Impuesto, Motivo Señoreaje y Motivo Deuda.",
            "Motivo Inflación, Motivo Deflación y Motivo Equilibrio."
        ],
        "correct_index": 1,
        "explanation": "Keynes desagrega la demanda monetaria en motivos dependientes del ingreso corriente (Transacción y Precaución, L1) y un motivo dependiente de la tasa de interés (Especulación, L2)."
    },
    {
        "id": "keynes_3",
        "question": "¿De qué variables depende el componente L1 (motivos transacción y precaución) en la función de demanda keynesiana?",
        "options": [
            "Exclusivamente de la varianza en los precios bursátiles de las acciones.",
            "Principalmente del nivel de ingreso corriente Y, siendo una función directa y positiva dL1/dY > 0.",
            "Inversamente de la tasa de descuento fijada por el Banco Central.",
            "De la semielasticidad de la inflación esperada de largo plazo."
        ],
        "correct_index": 1,
        "explanation": "L1 cubre la brecha temporal entre ingresos y gastos rutinarios y previene contingencias imprevistas. Ambas motivaciones dependen directamente del nivel de ingreso agregado corriente Y."
    },
    {
        "id": "keynes_4",
        "question": "¿Cuál es la causa subyacente que origina el motivo especulación (L2) en la teoría de Keynes?",
        "options": [
            "El deseo de los comerciantes de evadir el pago de impuestos aduaneros.",
            "La incertidumbre sobre la evolución futura de la tasa de interés de mercado y el riesgo de pérdida de capital en bonos.",
            "La escasez física de billetes de baja denominación impresos por la casa de moneda.",
            "La búsqueda de rendimientos dividendarios en activos de capital físico."
        ],
        "correct_index": 1,
        "explanation": "El motivo especulación nace de la elección de cartera entre dinero líquido (rendimiento cero, capital seguro) y bonos (pagan interés pero sufren riesgo de pérdida de capital si la tasa de interés sube)."
    },
    {
        "id": "keynes_5",
        "question": "Si la tasa de interés de mercado actual (r) es sumamente baja respecto a lo que el público considera su nivel 'normal', ¿qué conducta predice Keynes?",
        "options": [
            "El público comprará masivamente bonos esperando que la tasa caiga a cero.",
            "El público preferirá retener dinero líquido, previendo que la tasa subirá y causará pérdidas de capital en los bonos.",
            "El público aumentará de inmediato la inversión en maquinarias industriales.",
            "La demanda de dinero por motivo especulación descenderá a cero."
        ],
        "correct_index": 1,
        "explanation": "Cuando r está por debajo de lo 'normal', los agentes anticipan que solo puede subir. Como una suba de tasas derrumba el precio de los títulos de deuda, los inversores huyen hacia el dinero líquido (dL2/dr < 0)."
    },
    {
        "id": "keynes_6",
        "question": "¿Qué define conceptualmente a la 'Trampa de Liquidez' (Liquidity Trap)?",
        "options": [
            "Una situación donde los bancos comerciales cierran sus ventanillas por pánicos bancarios.",
            "Un tramo de la curva de demanda de dinero infinitamente elástico a una tasa críticamente baja, donde la política monetaria no puede bajar más la tasa.",
            "La quiebra simultánea de todas las empresas exportadoras por atraso cambiario.",
            "Un encaje legal del 100% que impide a los bancos otorgar préstamos al consumo."
        ],
        "correct_index": 1,
        "explanation": "A tasas mínimas cercanas a cero, el costo de oportunidad de mantener dinero es nulo y el riesgo de bonos es máximo. La curva de preferencia por la liquidez se vuelve horizontal y absorbe cualquier emisión monetaria sin reducir el interés."
    },
    {
        "id": "keynes_7",
        "question": "¿En qué se diferencia radicalmente la concepción keynesiana de la tasa de interés de la doctrina clásica prekeynesiana?",
        "options": [
            "Para Keynes es un fenómeno real que equilibra ahorro e inversión física; para los clásicos es monetaria.",
            "Para Keynes es un fenómeno estrictamente monetario (el precio por renunciar a la liquidez); para los clásicos era un fenómeno real del ahorro.",
            "Keynes sostiene que la tasa de interés no existe en el equilibrio general de corto plazo.",
            "Ambos coincidían en que la tasa de interés estaba determinada exclusivamente por la tasa de inflación."
        ],
        "correct_index": 1,
        "explanation": "Para los clásicos el interés remuneraba la abstinencia física del consumo; para Keynes es la recompensa puramente monetaria por desprenderse del control de la liquidez durante un lapso de tiempo."
    },
    {
        "id": "keynes_8",
        "question": "¿Qué es la Eficiencia Marginal del Capital (EMgK) en el esquema de la Teoría General?",
        "options": [
            "La relación técnica insumo-producto en las fábricas de bienes de consumo.",
            "La tasa de descuento que iguala el precio de oferta de un bien de capital con el valor presente de sus rendimientos netos esperados.",
            "La tasa de interés que cobran los prestamistas informales en los mercados no regulados.",
            "El margen de beneficio bruto obtenido en el último balance contable anual."
        ],
        "correct_index": 1,
        "explanation": "La EMgK sintetiza las expectativas empresariales sobre los flujos netos futuros generados por una unidad adicional de capital físico. La inversión se expande mientras la EMgK sea superior a la tasa de interés r."
    },
    {
        "id": "keynes_9",
        "question": "¿A qué atribuye Keynes el colapso de la actividad económica durante la Gran Depresión de 1929?",
        "options": [
            "A una rigidez institucional de salarios reales impuesta por sindicatos comunistas.",
            "Al derrumbe violento de la Eficiencia Marginal del Capital provocado por el pesimismo empresarial y el shock en los espíritus animales.",
            "A una sobreproducción permanente generada por la Ley de Say en los mercados agrícolas.",
            "A un exceso de gasto público que desplazó por crowding-out a los inversores privados."
        ],
        "correct_index": 1,
        "explanation": "El motor de las crisis es la volatilidad psicológica de la inversión privada: al desplomarse las expectativas sobre la rentabilidad futura del capital (EMgK) frente a una tasa de interés rígida, la inversión colapsa."
    },
    {
        "id": "keynes_10",
        "question": "¿Por qué Keynes rechaza que la baja de salarios nominales pueda solucionar el desempleo involuntario masivo?",
        "options": [
            "Porque los trabajadores demandarían el cierre de las fábricas.",
            "Porque reducir los salarios contrae la demanda efectiva global, deprimiendo las ventas y agravando la recesión.",
            "Porque en el patrón oro los salarios estaban fijados en gramos de metal.",
            "Porque los precios de las materias primas subirían instantáneamente compensando el salario."
        ],
        "correct_index": 1,
        "explanation": "Si todos los empresarios bajan los salarios nominales, destruyen el ingreso de las familias y la masa salarial de consumo. La demanda agregada se derrumba, forzando nuevos despidos en espiral."
    },
    {
        "id": "keynes_11",
        "question": "¿Qué concepto teórico define Keynes como la 'demanda efectiva'?",
        "options": [
            "La cantidad de billetes impresos que se encuentran depositados en bóvedas bancarias.",
            "El punto de intersección entre la curva de demanda global y la oferta global agregada que determina el nivel de empleo real.",
            "El volumen de importaciones requeridas por el sector industrial manufacturero.",
            "El total de crédito comercial autorizado por las juntas directivas bancarias."
        ],
        "correct_index": 1,
        "explanation": "La demanda efectiva es el nivel de gasto monetario que los empresarios efectivamente esperan captar del mercado. Determina el volumen de producción y puede estabilizarse en equilibrio con desempleo masivo."
    },
    {
        "id": "keynes_12",
        "question": "En condiciones de capacidad instalada ociosa y desempleo involuntario, ¿qué efecto genera una expansión monetaria o fiscal según Keynes?",
        "options": [
            "Produce inflación inmediata 1:1 en todos los precios de los bienes.",
            "Estimula la producción física y el empleo con precios y salarios relativamente constantes.",
            "Genera una catástrofe deflacionaria por aumento del ahorro privado forzoso.",
            "Destruye el multiplicador del comercio exterior mediante devaluación."
        ],
        "correct_index": 1,
        "explanation": "Habiendo fábricas paradas y desocupación, un incremento en el gasto arrastra la producción real y el empleo sin generar presiones inflacionarias significativas en costos."
    },
    {
        "id": "keynes_13",
        "question": "¿Cuándo se produce, según Keynes, lo que él denomina 'Inflación Verdadera' (True Inflation)?",
        "options": [
            "Cada vez que el Banco Central incrementa el circulante un 1% anual.",
            "Única y exclusivamente cuando la economía alcanza el pleno empleo físico de todos los factores de producción.",
            "Cuando el gobierno decreta aumentos en el salario mínimo legal.",
            "Cuando las exportaciones superan en valor monetario a las importaciones."
        ],
        "correct_index": 1,
        "explanation": "Solo cuando se agota la capacidad ociosa (pleno empleo), la curva de oferta agregada se vuelve perfectamente vertical. Todo nuevo gasto monetario a partir de allí es incapaz de generar producto y eleva los precios proporcionalmente."
    },
    {
        "id": "keynes_14",
        "question": "¿Por qué Keynes considera que la política monetaria es asimétrica y relativamente ineficaz durante depresiones severas?",
        "options": [
            "Porque los bancos comerciales tienen prohibido prestar dinero a menos del 10% anual.",
            "Porque abaratar el crédito no induce a los empresarios a invertir si sus expectativas sobre las ventas futuras (EMgK) están destruidas.",
            "Porque la política monetaria solo puede ser aplicada por el Congreso de la Nación.",
            "Porque la velocidad del dinero se vuelve infinita durante las crisis bancarias."
        ],
        "correct_index": 1,
        "explanation": "Aunque el Banco Central ofrezca crédito a tasa casi cero, si los empresarios ven un futuro sombrío y no esperan vender nada, no pedirán préstamos para comprar maquinaria nueva."
    },
    {
        "id": "keynes_15",
        "question": "¿Cuál es la prescripción de política económica prioritaria de Keynes para superar una depresión persistente?",
        "options": [
            "Equilibrio fiscal estricto y recorte drástico del gasto público.",
            "Política fiscal expansiva: obra pública y 'socialización de la inversión' financiada con déficit presupuestario.",
            "Aumentar el coeficiente de encaje bancario al 100% para evitar corridas.",
            "Esperar la liquidación automática de inventarios de acuerdo a la Ley de Say."
        ],
        "correct_index": 1,
        "explanation": "El Estado debe asumir el liderazgo de la demanda efectiva ejecutando gasto público financiado con endeudamiento, estimulando la reactivación a través del multiplicador del gasto."
    },
    {
        "id": "keynes_16",
        "question": "En el Capítulo 12 de la Teoría General, ¿cómo describe Keynes la toma de decisiones financieras en la Bolsa de Valores?",
        "options": [
            "Como un cálculo actuarial perfecto de los flujos de fondos descontados de las empresas a 50 años.",
            "Como un 'concurso de belleza', donde los inversores no eligen la acción más sólida sino la que creen que los demás van a elegir.",
            "Como un equilibrio walrasiano sin fricciones informacionales de ningún tipo.",
            "Como una aplicación estricta del teorema de Bayes para series estadísticas continuas."
        ],
        "correct_index": 1,
        "explanation": "Analogía del concurso de belleza periodístico: no gana la cara más bella en términos objetivos, sino la que cada concursante calcula que la mayoría considerará más bella (especulación de segundo orden)."
    },
    {
        "id": "keynes_17",
        "question": "¿Qué distinción epistemológica fundamental introduce Keynes entre 'Riesgo' e 'Incertidumbre'?",
        "options": [
            "El riesgo se aplica a las microempresas y la incertidumbre al gobierno federal.",
            "El riesgo puede calcularse con probabilidades matemáticas objetivas; en la incertidumbre genuina 'simplemente, no sabemos'.",
            "El riesgo no genera costos financieros y la incertidumbre eleva la prima de emisión.",
            "No existe ninguna distinción teórica; ambos términos son sinónimos matemáticos."
        ],
        "correct_index": 1,
        "explanation": "El riesgo admite distribuciones de frecuencia conocidas (lotería, seguros). Para el futuro histórico de inversiones irrepetibles, no hay base matemática objetiva: la incertidumbre es radical."
    },
    {
        "id": "keynes_18",
        "question": "¿Qué rol juegan las 'convenciones' en el comportamiento de los agentes bajo el marco keynesiano?",
        "options": [
            "Son acuerdos monopolísticos secretos sancionados por las leyes de defensa de la competencia.",
            "Son reglas prácticas precarias que consisten en asumir que el presente continuará indefinidamente igual, hasta que ocurra un shock.",
            "Son tratados internacionales de comercio que regulan el precio de las divisas.",
            "Son contratos laborales indexados obligatoriamente a la tasa de interés."
        ],
        "correct_index": 1,
        "explanation": "Para no paralizarse por la ignorancia del futuro, los agentes adoptan la convención de extrapolar el presente y seguir a la manada. Cuando una perturbación quiebra la convención, surge el pánico y la huida a la liquidez."
    },
    {
        "id": "keynes_19",
        "question": "¿Cómo se define el Multiplicador de la Inversión ideado originalmente por Richard Kahn e incorporado por Keynes?",
        "options": [
            "k = 1 / (1 - c), donde c es la propensión marginal a consumir.",
            "k = (c + 1) / (c + r), donde r es el encaje bancario legal.",
            "k = Yp / W, donde W es la riqueza humana de largo plazo.",
            "k = b · Y / (2r), derivado de los costos de corretaje bancario."
        ],
        "correct_index": 0,
        "explanation": "k = 1 / (1 - c) = 1 / s (donde s es la propensión al ahorro). Una inyección de inversión multiplica el ingreso en función de la fracción del ingreso que se destina al consumo en cada ronda."
    },
    {
        "id": "keynes_20",
        "question": "¿Cuál es la principal limitación que presenta el marco teórico de la Teoría General para analizar economías en desarrollo?",
        "options": [
            "Que asume que no existe el dinero metálico en ningún país del mundo.",
            "Que fue diseñado para economías industriales maduras con desempleo cíclico y capacidad ociosa, y no para países con escasez estructural de capital.",
            "Que rechaza las matemáticas y no formula ninguna ecuación analítica.",
            "Que exige que el Banco Central sea absorbido por los bancos comerciales privados."
        ],
        "correct_index": 1,
        "explanation": "En países subdesarrollados no existe un stock excedente de fábricas esperando demanda efectiva; existe una escasez material de capital productivo, tecnología e infraestructura que no se resuelve con simple estímulo fiscal al consumo."
    }
]

# 3. ROBERT LUCAS JR. (& SARGENT / WALLACE)
questions_bank["lucas"] = [
    {
        "id": "lucas_1",
        "question": "¿Cuál es la premisa metodológica definitoria de la Hipótesis de Expectativas Racionales (HER) formulada por Muth e introducida por Lucas?",
        "options": [
            "Los agentes disponen de poderes clarividentes que eliminan cualquier posibilidad de error empírico.",
            "Las expectativas subjetivas de los agentes coinciden con la esperanza matemática condicional del verdadero modelo objetivo de la economía.",
            "Los agentes corrigen sus errores ponderando el promedio aritmético de la inflación de los últimos 20 años.",
            "Las empresas forman expectativas copiando pasivamente los boletines oficiales de prensa del Banco Central."
        ],
        "correct_index": 1,
        "explanation": "Bajo HER, Et-1[Xt] = E[Xt | It-1]. Los agentes procesan eficientemente toda la información y conocen la estructura económica, por lo que sus previsiones subjetivas no tienen sesgos sistemáticos."
    },
    {
        "id": "lucas_2",
        "question": "¿Qué propiedad matemática exhiben los errores de pronóstico bajo expectativas racionales?",
        "options": [
            "Son errores acumulativos con autocorrelación serial fuertemente positiva.",
            "Son ruido blanco puramente estocástico con esperanza matemática cero y ortogonales a la información previa.",
            "Son proporcionales al coeficiente de encaje bancario fraccionario.",
            "Crecen exponencialmente al ritmo del multiplicador del gasto fiscal."
        ],
        "correct_index": 1,
        "explanation": "Los errores de predicción εt = Xt - Et-1[Xt] son no correlacionados, impredecibles y con media cero. Si contuvieran información sistemática, los agentes racionales la aprovecharían inmediatamente."
    },
    {
        "id": "lucas_3",
        "question": "¿Cómo se formaliza la Curva de Oferta Agregada de Lucas (1972)?",
        "options": [
            "yt = yn + α · (Pt - Et-1[Pt])",
            "yt = yn - α · (Mt - Bt)",
            "yt = yn + β · (rm - rb)",
            "yt = yn / (1 + πe)"
        ],
        "correct_index": 0,
        "explanation": "El producto yt solo se desvía de su nivel natural yn si existe una 'sorpresa' o error en la predicción de precios (Pt - Et-1[Pt]). Sin sorpresa, yt = yn."
    },
    {
        "id": "lucas_4",
        "question": "En el célebre 'Modelo de las Islas' de Lucas (1972), ¿qué mecanismo genera las fluctuaciones transitorias de producción?",
        "options": [
            "Un problema de 'extracción de señales': los productores confunden un shock inflacionario general con un aumento de la demanda relativa de su propio bien.",
            "La quiebra simultánea de los barcos comerciales que transportan mercancías entre las islas.",
            "Una suba unilateral de salarios impuesta por un sindicato centralizado inter-islas.",
            "La negativa de los bancos a prestar liquidez por agotamiento de reservas de oro."
        ],
        "correct_index": 0,
        "explanation": "Con información incompleta, el productor observa la suba del precio de su producto pero no el nivel general de precios. Cree que su precio relativo mejoró y eleva transitoriamente su producción hasta enterarse de la inflación general."
    },
    {
        "id": "lucas_5",
        "question": "¿Cuál es la predicción de la Nueva Macroeconomía Clásica respecto a los efectos de una emisión monetaria TOTALMENTE ANTICIPADA?",
        "options": [
            "Reduce el desempleo durante un período de al menos 5 años.",
            "Se traslada 1:1 a los precios nominales sin alterar el producto real ni el empleo, incluso en el muy corto plazo.",
            "Provoca una caída violenta en la tasa natural de interés de la economía.",
            "Genera un aumento masivo en la inversión en maquinarias industriales."
        ],
        "correct_index": 1,
        "explanation": "Si la política monetaria es anticipada, Pt = Et-1[Pt], por lo que el término de sorpresa se anula. El dinero es estrictamente neutral tanto a largo como a corto plazo frente a anuncios creíbles."
    },
    {
        "id": "lucas_6",
        "question": "¿Qué establece la 'Proposición de Ineficacia de la Política' (PIP) formulada por Thomas Sargent y Neil Wallace (1975)?",
        "options": [
            "Que ningún gobierno puede recaudar impuestos sin la autorización previa del parlamento.",
            "Que cualquier regla de política monetaria sistemática o previsible es totalmente ineficaz para estabilizar el producto y el empleo.",
            "Que las políticas fiscales expansivas siempre generan superávit presupuestario.",
            "Que los bancos comerciales no pueden quebrar bajo regímenes de convertibilidad metálica."
        ],
        "correct_index": 1,
        "explanation": "Cualquier regla determinista o sistemática contracíclica del Banco Central es incorporada por el público racional en sus expectativas, neutralizando completamente su efecto estabilizador en la producción real."
    },
    {
        "id": "lucas_7",
        "question": "En su artículo seminal de 1976, ¿en qué consiste la demoledora 'Crítica de Lucas'?",
        "options": [
            "En demostrar que los ordenadores electrónicos cometían errores de redondeo al calcular el PBI.",
            "En advertir que los parámetros de los modelos macroeconométricos tradicionales no son estructurales, pues cambian cuando cambia el régimen de política.",
            "En criticar a los economistas por utilizar funciones logarítmicas en la demanda de dinero.",
            "En probar que los bancos centrales falseaban intencionalmente las series históricas de base monetaria."
        ],
        "correct_index": 1,
        "explanation": "Los parámetros estimados en modelos econométricos históricos dependen de las reglas de política vigentes en ese período. Si el gobierno altera su política, los agentes racionales modifican su comportamiento y los parámetros cambian, invalidando la predicción."
    },
    {
        "id": "lucas_8",
        "question": "Para superar la Crítica de Lucas, ¿qué requisito metodológico obligatorio exigió la Nueva Macroeconomía Clásica a los modelos?",
        "options": [
            "Que se basen en encuestas de opinión callejeras a gran escala.",
            "Que posean microfundamentos rigurosos: deriven de funciones de utilidad de hogares y funciones de producción de firmas que optimizan intertemporalmente.",
            "Que eliminen por completo las variables monetarias y financieras de las ecuaciones.",
            "Que utilicen exclusivamente datos trimestrales de economías sin bancos comerciales."
        ],
        "correct_index": 1,
        "explanation": "Para que los parámetros sean estructurales e invariantes a las políticas, deben reflejar los 'fundamentos profundos': preferencias psicológicas de utilidad, aversión al riesgo, tasas de descuento y restricciones tecnológicas."
    },
    {
        "id": "lucas_9",
        "question": "¿En qué consiste el problema de la 'Inconsistencia Temporal' analizado por Kydland y Prescott (1977) en el marco de expectativas racionales?",
        "options": [
            "En la dificultad física de registrar las transacciones financieras en tiempo real.",
            "En el incentivo que tienen las autoridades a prometer inflación baja pero generar sorpresas inflacionarias ex post para bajar el desempleo transitoriamente.",
            "En la discrepancia entre el calendario gregoriano y los ejercicios fiscales estatales.",
            "En la incapacidad del público para recordar las promesas electorales pasadas."
        ],
        "correct_index": 1,
        "explanation": "Un plan óptimo formulado ex ante no es consistente en el tiempo si el gobierno tiene discrecionalidad: una vez fijados los salarios, el gobierno se ve tentado a emitir para bajar el desempleo."
    },
    {
        "id": "lucas_10",
        "question": "¿Cuál es la consecuencia directa de la discrecionalidad gubernamental bajo inconsistencia temporal?",
        "options": [
            "Un equilibrio con pleno empleo permanente y deflación sostenida.",
            "La generación de un 'sesgo inflacionario' (inflation bias) permanente sin reducción del desempleo.",
            "La eliminación voluntaria de la deuda pública soberana.",
            "El colapso de la recaudación tributaria al 0% del PBI."
        ],
        "correct_index": 1,
        "explanation": "El público anticipa el incentivo al engaño de la autoridad y exige aumentos preventivos de salarios y precios. El resultado final es más inflación sin ninguna mejora en el empleo."
    },
    {
        "id": "lucas_11",
        "question": "¿Cuál es la solución institucional recomendada por la literatura nuevo-clásica frente a la inconsistencia temporal?",
        "options": [
            "Nombrar políticos de izquierda en los ministerios de hacienda.",
            "Adoptar reglas constitucionales de política y consagrar la independencia de Bancos Centrales gobernados por banqueros centrales conservadores (Rogoff).",
            "Aumentar la discrecionalidad del poder ejecutivo para decretar emisiones extraordinarias.",
            "Nacionalizar todo el sistema bancario comercial."
        ],
        "correct_index": 1,
        "explanation": "Delegar la conducción monetaria en un Banco Central independiente y con aversión a la inflación otorga credibilidad al compromiso de estabilidad, eliminando el sesgo inflacionario."
    },
    {
        "id": "lucas_12",
        "question": "¿Qué supuesto básico sobre el funcionamiento de los mercados sostiene la Nueva Macroeconomía Clásica?",
        "options": [
            "Rigidez total de precios y salarios a la baja durante décadas.",
            "Vaciado continuo de mercados (market clearing): todos los precios y salarios se ajustan instantáneamente para igualar oferta y demanda.",
            "Existencia permanente de racionamiento burocrático de mercancías.",
            "Monopolios estatales en la fijación de todas las tasas de interés."
        ],
        "correct_index": 1,
        "explanation": "Asumen el equilibrio walrasiano: los precios son flexibles y vacían los mercados de bienes y factores en cada momento; no hay desequilibrios involuntarios ni excesos persistentes de oferta."
    },
    {
        "id": "lucas_13",
        "question": "¿Cómo conciben el desempleo observado los modelos nuevo-clásicos estándar?",
        "options": [
            "Como una falla trágica e involuntaria del sistema de precios libres.",
            "Como una elección voluntaria de sustitución intertemporal del ocio por trabajo frente a shocks de salarios reales esperados.",
            "Como la consecuencia exclusiva de los convenios laborales colectivos de los sindicatos.",
            "Como un fenómeno originado en la escasez de papel moneda fiduciario."
        ],
        "correct_index": 1,
        "explanation": "El desempleo se interpreta como una decisión óptima de optimización intertemporal: los trabajadores reducen voluntariamente su oferta de trabajo hoy cuando perciben salarios reales transitoriamente bajos."
    },
    {
        "id": "lucas_14",
        "question": "¿Qué modelo de demanda de dinero formal se asocia frecuentemente con Robert Lucas?",
        "options": [
            "El modelo de balances de caja de Marshall.",
            "El modelo de dinero por adelantado (Cash-in-Advance model de Clower y Lucas).",
            "La teoría de inventarios de Baumol y Tobin.",
            "El enfoque del circuito monetario postkeynesiano."
        ],
        "correct_index": 1,
        "explanation": "Lucas formaliza el dinero introduciendo una restricción técnica de Cash-in-Advance: las familias deben poseer liquidez en efectivo antes de concurrir al mercado para poder adquirir bienes de consumo."
    },
    {
        "id": "lucas_15",
        "question": "¿En qué evolucionó la Nueva Macroeconomía Clásica en los años 80 bajo la dirección de Kydland y Prescott?",
        "options": [
            "Hacia la Teoría Monetaria Moderna (MMT).",
            "Hacia la Teoría de los Ciclos Económicos Reales (Real Business Cycles - RBC).",
            "Hacia el Marxismo Analítico de Cambridge.",
            "Hacia la Teoría de la Represión Financiera de Stanford."
        ],
        "correct_index": 1,
        "explanation": "La escuela RBC prescindió de las sorpresas monetarias y postuló que los ciclos económicos son el resultado óptimo de equilibrio de agentes ante shocks estocásticos reales en la productividad tecnológica."
    },
    {
        "id": "lucas_16",
        "question": "En la teoría de ciclos reales (RBC), ¿cuál es el papel asignado al dinero en la propagación del ciclo?",
        "options": [
            "Es el motor originario de todos los auges y recesiones.",
            "Es puramente neutral y endógeno: la correlación positiva dinero-producto refleja que la actividad real demanda más dinero (causalidad inversa).",
            "Es el único responsable de la tasa natural de desempleo.",
            "Provoca pánicos bancarios trimestrales predecibles."
        ],
        "correct_index": 1,
        "explanation": "Para RBC el dinero es superneutral. Si se observa que M y PBI crecen juntos, es porque el auge real induce una mayor demanda transaccional bancaria endógena (causalidad inversa a la monetarista)."
    },
    {
        "id": "lucas_17",
        "question": "¿Por qué Robert Lucas critica severamente los modelos de la síntesis keynesiana IS-LM?",
        "options": [
            "Porque no utilizaban el idioma inglés en sus publicaciones académicas.",
            "Porque carecen de microfundamentos de optimización intertemporal y asumen expectativas ad-hoc retrospectivas no racionales.",
            "Porque los modelos IS-LM no admiten la existencia de bonos del gobierno.",
            "Porque la curva IS no contempla el pago de salarios nominales en efectivo."
        ],
        "correct_index": 1,
        "explanation": "Para Lucas, las curvas IS-LM agregadas son ecuaciones empíricas sin base en decisiones óptimas de hogares y empresas que maximizan bajo restricciones dinámicas."
    },
    {
        "id": "lucas_18",
        "question": "¿Qué diferencia sustancial existe entre la crítica de Lucas a las expectativas y la postura previa de Friedman?",
        "options": [
            "Friedman no creía en las estadísticas empíricas del dinero.",
            "Friedman utilizaba expectativas adaptativas (mirada al pasado), mientras que Lucas introduce expectativas racionales (mirada prospectiva a las reglas de política).",
            "Lucas defendía el control de M2 propuesto por Friedman.",
            "Friedman sostenía que la curva de Phillips era horizontal y Lucas que era vertical."
        ],
        "correct_index": 1,
        "explanation": "Bajo expectativas adaptativas de Friedman, la autoridad aún podía engañar sistemáticamente a la economía acelerando la emisión. Bajo expectativas racionales de Lucas, el público anticipa la regla y el engaño desaparece."
    },
    {
        "id": "lucas_19",
        "question": "¿Cómo se modela el sistema bancario en los modelos macroeconómicos estándar de Lucas y la escuela nuevo-clásica?",
        "options": [
            "Como una entidad monopólica estatal que raciona administrativamente los fondos.",
            "Como intermediarios financieros transparentes y sin fricciones bajo condiciones del teorema de Modigliani-Miller agregado.",
            "Como una fuente permanente de pánicos de liquidez y externalidades destructivas.",
            "Como cooperativas de crédito sin fines de lucro."
        ],
        "correct_index": 1,
        "explanation": "Al asumir información perfecta y mercados completos, la estructura bancaria no altera las decisiones reales de equilibrio intertemporal; el crédito es un simple velo financiero."
    },
    {
        "id": "lucas_20",
        "question": "¿Por qué los modelos nuevo-clásicos recibieron fuertes críticas tras la crisis financiera de 2008?",
        "options": [
            "Porque no contemplaban el cálculo de la tasa de interés en términos nominales.",
            "Porque al asumir mercados financieros sin fricciones ni riesgo sistémico, fueron ciegos ante la fragilidad de los bancos y el colapso del crédito real.",
            "Porque exigían el retorno obligatorio al patrón oro internacional.",
            "Porque predecían que la inflación alcanzaría el 1000% anual en los Estados Unidos."
        ],
        "correct_index": 1,
        "explanation": "Al excluir las asimetrías de información, los balances bancarios, el colateral y las corridas de liquidez, los modelos DSGE estándar no pudieron prever ni explicar el contagio financiero de 2008."
    }
]

# Import parts 1 and 2
from questions_part1 import bank_part1
from questions_part2 import bank_part2

# Merge all questions
full_bank = {}
full_bank.update(questions_bank)
full_bank.update(bank_part1)
full_bank.update(bank_part2)

print(f"Total economistas cargados: {len(full_bank)}")
total_q = 0
for econ, q_list in full_bank.items():
    print(f"  - {econ}: {len(q_list)} preguntas")
    total_q += len(q_list)
print(f"Total de preguntas teóricas generadas: {total_q}")

# Metadata
export_data = {
    "metadata": {
        "title": "Banco de Exámenes Teóricos de Sistemas Bancarios y Teoría Monetaria",
        "description": "20 preguntas teóricas multiple choice por economista para preparación de examen universitario",
        "total_economists": len(full_bank),
        "total_questions": total_q
    },
    "questions_by_economist": full_bank
}

# Save JSON in root and static
with open("exam_questions.json", "w", encoding="utf-8") as f:
    json.dump(export_data, f, ensure_ascii=False, indent=2)

with open("static/exam_questions.json", "w", encoding="utf-8") as f:
    json.dump(export_data, f, ensure_ascii=False, indent=2)

# Save JS in root and static
js_content = f"window.EXAM_QUESTIONS = {json.dumps(export_data, ensure_ascii=False, indent=2)};"
with open("exam_questions.js", "w", encoding="utf-8") as f:
    f.write(js_content)

with open("static/exam_questions.js", "w", encoding="utf-8") as f:
    f.write(js_content)

print("¡Archivos exam_questions.js y exam_questions.json creados con éxito en raíz y static!")


# -*- coding: utf-8 -*-
"""
add_exam_keys_data.py
Genera las 14 Claves Maestras para el Examen Universitario con desglose analítico profundo:
- Título y doctrina clave
- ¿Por qué es clave para el examen? (criterio docente)
- Trampa habitual del estudiante (error común a evitar)
- Respuesta de 10 universitario (conceptos y palabras clave obligatorias)
- Mecanismo analítico y deducción formal / fórmula
- Contraste doctrinal obligatorio
- Enlaces y referencias a los textos y preguntas de examen
"""

import json

EXAM_KEYS = [
    {
        "id": "clave_1_friedman_inflacion",
        "number": 1,
        "economist_id": "friedman",
        "economist_name": "Milton Friedman",
        "school": "Monetarismo / Escuela de Chicago",
        "topic_id": "t3_inflacion",
        "topic_name": "Inflación y Estabilidad de Precios",
        "source_texts": [
            "Facu 100 Friedman-2496353.pdf (Inflation and Unemployment)",
            "Facu 96 Argandoña- Friedman.pdf (Monetarismo)"
        ],
        "title": "Refutación de Causas No Monetarias de la Inflación y la Naturaleza Estrictamente Monetaria del Fenómeno",
        "the_key": "La inflación es en todo momento y lugar un fenómeno estrictamente monetario, generado exclusivamente por una tasa de expansión de la cantidad de dinero más rápida que la del producto real. Las presiones sindicales, los shocks petroleros y el déficit fiscal por sí solos son incapaces de generar inflación sostenida sin convalidación monetaria.",
        "why_is_key": "Es la pregunta conceptual obligatoria de la cátedra para evaluar si el alumno entiende la distinción entre un cambio puntual en los 'precios relativos' y un aumento sostenido en el 'nivel general de precios' (P). Los profesores suelen presentar enunciados trampa con shocks de costos o desequilibrios fiscales para observar si el estudiante cae en la explicación de costos o si fundamenta la restricción monetaria cuantitativa.",
        "typical_exam_trap": "Sostener que un aumento salarial agresivo de los sindicatos o un shock internacional del petróleo (OPEP) 'causa inflación'. Para Friedman, si la masa monetaria M permanece constante, el shock de un bien solo reduce la demanda y los precios de los restantes bienes, o provoca desempleo transitorio, pero NUNCA un incremento continuo y generalizado de P.",
        "university_answer": "El alumno debe responder: 'Un shock de costos o un déficit fiscal solo produce inflación si el Banco Central lo convalida monetariamente emitiendo dinero para financiarlo o para evitar el desempleo transitorio. Sin expansión monetaria, el aumento del precio del petróleo o de los salarios solo genera un cambio en los precios relativos (p_i / P), forzando una reducción en los precios o cantidades de otros sectores. La inflación sostenida requiere necesariamente ΔM/M > ΔY/Y'. Citar la estabilidad de la función de demanda de dinero en el largo plazo.",
        "theoretical_mechanism": "Partiendo de la identidad cuantitativa en tasas de variación: \\( \\dot{P} = \\dot{M} + \\dot{V} - \\dot{Y} \\). Dado que la velocidad \\( V \\) está determinada por variables estructurales de riqueza y carteras que son altamente estables empíricamente (Friedman & Schwartz), en el largo plazo \\( \\dot{V} \\approx 0 \\). Si el producto de pleno empleo crece al ritmo potencial \\( \\dot{Y}_n \\), entonces \\( \\pi = \\dot{P} = \\dot{M} - \\dot{Y}_n \\). Cualquier factor no monetario solo puede alterar \\( \\pi \\) si modifica transitoriamente \\( V \\) o \\( Y \\), pero no puede sostener una tasa positiva de inflación permanente.",
        "doctrinal_contrast": "Se contrapone directamente a la Teoría Estructuralista Latinoamericana (Olivera y Canavese), a las tesis poskeynesianas de inflación de costos y puja distributiva (Lorenzoni y Werning), y al enfoque fiscal puro sin convalidación."
    },
    {
        "id": "clave_2_friedman_definicion_dinero",
        "number": 2,
        "economist_id": "friedman",
        "economist_name": "Milton Friedman",
        "school": "Monetarismo / Escuela de Chicago",
        "topic_id": "t1_definicion_dinero",
        "topic_name": "Naturaleza y Definición del Dinero",
        "source_texts": [
            "Facu 96 Argandoña- Friedman.pdf",
            "Facu 100 Friedman-2496353.pdf"
        ],
        "title": "Criterio Instrumental y Pragmático de Selección de Agregados (M2) e Ingreso Permanente (Yp)",
        "the_key": "El dinero adecuado no debe definirse a priori en función de propiedades físicas, jurídicas de curso forzoso o atributos intrínsecos de liquidez inmediata, sino en función de un criterio instrumental: aquel agregado estadístico cuya relación con el ingreso nominal resulte empíricamente más estable y predictible.",
        "why_is_key": "Evalúa el método positivista de Friedman frente a la tradición de la Currency School y la Escuela Clásica. Permite indagar por qué Friedman y Schwartz eligieron M2 (incluyendo depósitos a plazo) en lugar de M1 en su monumental estudio 'A Monetary History of the United States', y por qué su restricción presupuestaria es la riqueza total (Ingreso Permanente Yp) y no el ingreso corriente keynesiano.",
        "typical_exam_trap": "Afirmar que Friedman define el dinero como M1 porque es el medio de pago directo que no paga interés, o creer que su teoría de la demanda de dinero es una teoría para predecir la producción y el empleo a corto plazo.",
        "university_answer": "Debe citarse taxativamente la máxima friedmaniana: 'La teoría cuantitativa es en primer lugar una teoría de la demanda de dinero; no es una teoría de la producción, ni del ingreso nominal, ni del nivel de precios'. Friedman demuestra que los depósitos a plazo fijo en bancos comerciales satisfacen la misma demanda de saldos de reserva del público que las cuentas corrientes, presentando una correlación estadística más estrecha con el ingreso nacional.",
        "theoretical_mechanism": "Función de demanda de dinero friedmaniana: \\( (M/P)^d = f(Y_p, w, r_m, r_b, r_e, \\frac{1}{P}\\frac{dP}{dt}, u) \\), donde \\( Y_p \\) es el Ingreso Permanente (aproximación de la riqueza total descontada \\( W = \\frac{Y_p}{r} \\)), \\( w \\) es la proporción de riqueza humana a no humana, y las tasas de rendimiento son respecto a bienes físicos y títulos. Como el dinero es considerado un activo de capital durable que rinde servicios productivos y de liquidez, su demanda es una función estable de pocos argumentos.",
        "doctrinal_contrast": "Se opone al formalismo legalista de la Currency School (que solo reconocía como dinero al oro y los billetes con curso legal) y al Informe Radcliffe (1959, que diluía el dinero en una liquidez general inasible de activos financieros)."
    },
    {
        "id": "clave_3_keynes_preferencia_liquidez",
        "number": 3,
        "economist_id": "keynes",
        "economist_name": "John Maynard Keynes",
        "school": "Keynesianismo / Escuela de Cambridge",
        "topic_id": "t2_demanda_dinero",
        "topic_name": "Demanda de Dinero y Tasa de Interés",
        "source_texts": [
            "Facu 108 De Keynes a Lucas.pdf",
            "Facu 97 Demanda de dinero.pdf"
        ],
        "title": "La Demanda Especulativa de Dinero, la Trampa de la Liquidez y la Tasa de Interés como Fenómeno Estrictamente Monetario",
        "the_key": "La tasa de interés no es la recompensa por la abstinencia o el ahorro de capital real (refutación de la teoría clásica del fondo prestable), sino el precio que equilibra el deseo de conservar la riqueza en forma líquida frente a formas ilíquidas. A tasas de interés críticamente bajas, la elasticidad de la demanda de dinero respecto a la tasa de interés tiende a infinito (Trampa de la Liquidez), anulando la efectividad de la política monetaria.",
        "why_is_key": "Es la ruptura epistemológica más trascendente de la 'Teoría General' (1936). Los docentes evalúan rigurosamente si el alumno comprende el motivo especulación ($L_2(r)$) derivado de la incertidumbre sobre el precio futuro de los bonos, y cómo este motivo destruye la autorregulación clásica hacia el pleno empleo.",
        "typical_exam_trap": "Explicar la demanda de dinero keynesiana limitándose al motivo transacción y precaución (que dependen del ingreso $Y$), o afirmar que en la trampa de la liquidez los agentes no demandan dinero porque la tasa de interés es baja (al contrario: demandan INFINITA liquidez porque esperan que la tasa solo pueda subir, lo que provocaría pérdidas de capital masivas en bonos).",
        "university_answer": "El alumno debe desglosar la función de demanda en dos componentes analíticos: \\( M^d = M_1(Y) + M_2(r) \\). En la Trampa de la Liquidez, la tasa de interés de mercado \\( r \\) ha alcanzado un piso mínimo absoluto donde el rendimiento de los títulos es insuficiente para compensar el riesgo de una caída en sus precios (pérdidas de capital \\( \\Delta P_b < 0 \\)). Por lo tanto, cualquier incremento en la oferta monetaria es absorbido por la demanda especulativa sin lograr reducir \\( r \\) ni estimular la inversión (invalidez de la política monetaria; necesidad prioritaria de la política fiscal expansiva).",
        "theoretical_mechanism": "Relación inversa entre precio de bonos y tasa de interés: \\( P_b = \\frac{C}{r} \\). Si la tasa actual \\( r \\) es percibida por debajo de la tasa 'normal' esperada \\( r_e \\), los agentes anticipan un aumento inminente de la tasa (\\( r \\uparrow \\)), lo cual implicará que el precio del bono caerá (\\( P_b \\downarrow \\)). Para evitar la pérdida de capital, los agentes venden títulos y atesoran dinero en efectivo: \\( \\frac{\\partial L_2}{\\partial r} \\to -\\infty \\).",
        "doctrinal_contrast": "Frente a los Clásicos (Fisher y Pigou, donde el interés es un fenómeno real de productividad y ahorro) y frente a Milton Friedman (para quien la trampa de la liquidez es una mera curiosidad analítica jamás observada empíricamente en la historia monetaria)."
    },
    {
        "id": "clave_4_lucas_critica_inefectividad",
        "number": 4,
        "economist_id": "lucas",
        "economist_name": "Robert Lucas Jr. (& Sargent / Wallace)",
        "school": "Nueva Macroeconomía Clásica",
        "topic_id": "t6_politica_monetaria",
        "topic_name": "Canales y Eficacia de la Política Monetaria",
        "source_texts": [
            "Facu 108 De Keynes a Lucas.pdf",
            "Facu 86 Ex ante y ex post.pdf"
        ],
        "title": "La Crítica de Lucas (1976) y la Proposición de Inefectividad de la Política Monetaria Sistemática",
        "the_key": "Los parámetros estimados en modelos macroeconométricos agregados tradicionales no son estructurales ni invariantes ante cambios de régimen de política económica, porque los agentes dotados de expectativas racionales ajustan óptimamente sus reglas de conducta ante cualquier intervención sistemática. En consecuencia, la política monetaria anticipada es completamente inefectiva para alterar el producto real y el empleo.",
        "why_is_key": "Constituye el núcleo de la revolución neoclásica de las expectativas racionales que sepultó el consenso de la síntesis neoclásica-keynesiana. En las mesas de examen se indaga exhaustivamente si el estudiante sabe por qué los gobiernos no pueden 'explotar' la Curva de Phillips para reducir sistemáticamente el desempleo.",
        "typical_exam_trap": "Sostener que Lucas afirma que el dinero 'nunca tiene efectos reales'. La clave precisa de examen es que la política monetaria SISTEMÁTICA o ANTICIPADA no tiene efectos sobre el producto; pero las 'sorpresas monetarias' no anticipadas sí generan efectos reales temporales debido al problema de extracción de señales (confusión entre shocks de precios relativos y nivel general en el modelo de islas).",
        "university_answer": "Debe citarse la Curva de Oferta Agregada de Lucas: \\( y_t = y_n + \\alpha (p_t - E_{t-1}[p_t]) + \\varepsilon_t \\). Si el Banco Central sigue una regla sistemática de política monetaria conocida por el público, los agentes forman su expectativa óptima utilizando toda la información disponible: \\( E_{t-1}[p_t] = p_t \\), haciendo que \\( (p_t - E_{t-1}[p_t]) = 0 \\) y por lo tanto \\( y_t = y_n + \\varepsilon_t \\). La política anticipada solo se traslada unívocamente a los precios sin alterar el producto real ni el desempleo.",
        "theoretical_mechanism": "Deducción de la Proposición de Inefectividad de Sargent y Wallace (1975): Dado \\( y_t = y_n + \\alpha (p_t - E_{t-1} p_t) \\) y la demanda agregada \\( m_t + v_t = p_t + y_t \\). Si la regla de dinero es \\( m_t = g_0 + g_1 x_{t-1} + u_t \\) donde \\( u_t \\) es ruido blanco no correlacionado, los agentes racionales fijan \\( E_{t-1} m_t = g_0 + g_1 x_{t-1} \\). La sorpresa monetaria es únicamente el choque aleatorio \\( u_t \\). Por ende, los coeficientes de retroalimentación de la política \\( g_1 \\) no afectan la distribución de probabilidad de \\( y_t \\).",
        "doctrinal_contrast": "Frente al Keynesianismo tradicional de Curva de Phillips estable (Samuelson y Solow) y frente al Monetarismo de Friedman (que admitía rezagos largos y variables donde la política monetaria podía desviar el producto durante años mediante expectativas adaptativas)."
    },
    {
        "id": "clave_5_bernanke_canal_credito",
        "number": 5,
        "economist_id": "bernanke",
        "economist_name": "Ben S. Bernanke (& Gertler / Gilchrist)",
        "school": "Nuevo Keynesianismo / Fricciones Financieras",
        "topic_id": "t5_crisis_fluctuaciones",
        "topic_name": "Crisis Financieras y el Canal del Crédito",
        "source_texts": [
            "Facu 102 Bernanke Nobel Lecture.pdf (Banking, Credit and the Macroeconomy)"
        ],
        "title": "El Canal del Crédito, el Acelerador Financiero y la Corrección Fundamental a Friedman sobre la Gran Depresión de 1929",
        "the_key": "La profundidad y persistencia de la Gran Depresión de 1929 no pueden explicarse satisfactoriamente solo mediante la contracción monetaria tradicional (M1 de Friedman y Schwartz), sino fundamentalmente por el colapso del sistema de intermediación bancaria, que destruyó el capital informacional sobre los deudores y disparó el Premio por Financiamiento Externo (External Finance Premium).",
        "why_is_key": "Pregunta de máxima calificación en exámenes de grado y posgrado. Los profesores evalúan la capacidad de distinguir el canal monetario tradicional (tasa de interés real en mercados de bonos sin fricciones) del canal de transmisión crediticia bancaria (asimetrías de información, selección adversa y costos de monitoreo de auditoría de Townsend).",
        "typical_exam_trap": "Decir que Bernanke 'refuta' a Friedman. La respuesta rigurosa es que Bernanke demuesta que el canal monetario puro de Friedman es insuficiente cuantitativamente: la quiebra masiva de casi 10.000 bancos provocó una crisis crediticia cualitativa que racionó a los prestatarios pequeños y medianos que no podían emitir títulos en Wall Street.",
        "university_answer": "El alumno debe definir con precisión el 'Premio por Financiamiento Externo' (EFP): la diferencia entre el costo de fondos obtenidos externamente y el costo de oportunidad de los fondos generados internamente. Debido a asimetrías de información, \\( EFP = s(NW) \\), donde \\( NW \\) es el patrimonio neto o colateral del prestatario (con \\( s' < 0 \\)). Cuando los shocks macroeconómicos deterioran los balances bancarios y el valor de los colaterales, el EFP se dispara, provocando un corte abrupto del crédito y una amplificación endógena de la recesión (el mecanismo del Acelerador Financiero).",
        "theoretical_mechanism": "Formalización del balance del prestatario: Los bancos enfrentan un costo de verificación estatal costosa (CSV de Townsend / Bernanke y Gertler 1989). Para prestar fondos a una empresa con activos \\( A \\) y patrimonio neto \\( NW \\), el banco exige un premio de financiamiento \\( EFP \\). Si el valor de los activos cae por deflación de deudas de Fisher: \\( NW \\downarrow \\implies EFP \\uparrow \\implies \\text{Inversión } I \\downarrow \\implies \\text{Producto } Y \\downarrow \\implies NW \\downarrow \\). El canal bancario consta de dos subcanales: el 'canal de préstamos bancarios' (oferta de crédito bancario) y el 'canal de la hoja de balance' (fortaleza patrimonial del prestatario).",
        "doctrinal_contrast": "Frente al Teorema Modigliani-Miller (que postula la neutralidad de la estructura financiera y la irrelevancia de los bancos) y frente a la visión estrictamente monetaria cuantitativa de Friedman & Schwartz."
    },
    {
        "id": "clave_6_banking_school_ley_reflujo",
        "number": 6,
        "economist_id": "banking_school",
        "economist_name": "Banking School (Thomas Tooke, John Fullarton)",
        "school": "Banking School (Escuela Bancaria)",
        "topic_id": "t4_sistema_bancario",
        "topic_name": "Sistema Bancario, Creación de Dinero y Regulación",
        "source_texts": [
            "Facu 174 Banking School.pdf (Arnon / Tooke & Fullarton)"
        ],
        "title": "La Ley del Reflujo (Law of Reflux) y la Imposibilidad de Sobreemisión de Billetes Convertibles",
        "the_key": "En un sistema monetario con convertibilidad estricta en metal precioso donde los bancos emiten billetes descontando pagarés y letras de cambio comerciales a corto plazo ('Real Bills'), es conceptual y prácticamente imposible que ocurra una sobreemisión de papel moneda que eleve los precios generales, pues el exceso de emisión refluye automáticamente al emisor.",
        "why_is_key": "Es la piedra angular de toda la literatura sobre dinero endógeno del siglo XIX y el antecedente fundamental de la teoría monetaria poskeynesiana. Pregunta recurrente en exámenes de Historia del Pensamiento Monetario: '¿Puede un banco comercial sobreemitir billetes convertibles según Fullarton y Tooke?'.",
        "typical_exam_trap": "Contestar afirmativamente basándose en la teoría cuantitativa. La respuesta de la Banking School es taxativamente NEGATIVA: ningún banco, ni siquiera el Banco de Inglaterra, puede forzar en la circulación más billetes de los que el público y el comercio voluntariamente desean mantener.",
        "university_answer": "El estudiante debe enunciar y explicar los dos mecanismos de la Ley del Reflujo de John Fullarton (1844): si un banco emite billetes que exceden las necesidades transaccionales del público, el exceso no permanece en el mercado elevando los precios, sino que regresa inexorablemente al emisor por dos vías: (1) Depósito bancario remunerado o amortización anticipada de deudas que los comerciantes tienen con el banco; o (2) Canje de billetes por oro metálico si la tasa de interés interna cae por debajo de la externa. Citar además la doctrina de las Letras Reales (Real Bills Doctrine) de Adam Smith y Thomas Tooke.",
        "theoretical_mechanism": "Secuencia de endogeneidad de Fullarton: \\( \\text{Demanda del Comercio y Precios } (P \\cdot T) \\to \\text{Descuento de Letras } \\to \\text{Emisión de Billetes } M \\). Si \\( M_{emitido} > M^d \\), la tasa de retorno de los fondos opera a través de los balances: los agentes cancelan créditos comerciales o convierten billetes a depósitos. La oferta monetaria es gobernada pasivamente por las necesidades del intercambio comercial.",
        "doctrinal_contrast": "Se opone radicalmente a la Currency School (Lord Overstone, Torrens, Norman), quienes sostenían que los bancos comerciales sí pueden sobreemitir y provocar depreciación cambiaria y drenaje de reservas áureas si no son sometidos a una regla metálica estricta."
    },
    {
        "id": "clave_7_currency_school_principio_metalico",
        "number": 7,
        "economist_id": "currency_school",
        "economist_name": "Currency School (Lord Overstone, Robert Torrens)",
        "school": "Currency School (Escuela Monetaria)",
        "topic_id": "t4_sistema_bancario",
        "topic_name": "Sistema Bancario y Regulación (Ley de Peel de 1844)",
        "source_texts": [
            "Facu 174 Banking School.pdf",
            "Facu 59 Sist. Bancarios y Cred..pdf"
        ],
        "title": "El Principio Metálico, la Regla del 100% de Respaldo y la Ley Bancaria de Robert Peel de 1844",
        "the_key": "El papel moneda fiduciario mixto debe fluctuar en volumen de manera exactamente idéntica a como fluctuaría una circulación compuesta puramente de metales preciosos (oro). Cualquier emisión de billetes por encima de un monto fiduciario rígido fijo debe tener respaldo áureo del 100%, debiendo separarse la emisión bancaria de la banca comercial ordinaria.",
        "why_is_key": "Explica el diseño institucional de los bancos centrales modernos y la Ley Bancaria británica de 1844 (Bank Charter Act). La cátedra examina si el estudiante comprende las razones doctrinarias de la separación del Banco de Inglaterra en dos departamentos y el gravísimo error teórico de la Currency School que llevó a las recurrentes suspensiones de la ley en las crisis de 1847, 1857 y 1866.",
        "typical_exam_trap": "No identificar la falla crucial de la Currency School: consideraron únicamente a los billetes bancarios impresos como 'dinero', ignorando por completo que los depósitos en cuenta corriente transferibles por cheque cumplían exactamente la misma función monetaria.",
        "university_answer": "El alumno debe detallar: (1) El principio de la moneda metálica pura (Lord Overstone); (2) La estructura impuesta por la Ley de Peel: creación del 'Issue Department' (autómata emisor con tope fiduciario de £14 millones respaldado en deuda pública y 100% en oro sobre cualquier excedente) y el 'Banking Department' (que operaba como banco comercial ordinario sin privilegios de emisión); (3) El fracaso estructural: al ignorar los depósitos a la vista, las crisis de liquidez forzaron al gobierno británico a suspender la ley en tres ocasiones para permitirle al Banco de Inglaterra emitir billetes sin respaldo de oro y evitar la quiebra total del sistema bancario londinense.",
        "theoretical_mechanism": "Mecanismo de ajuste precio-flujo de especie de Hume formalizado por la Currency School: Si hay salida de oro (\\( \\Delta Oro < 0 \\)), el Issue Department debe contraer la circulación de billetes exactamente en la misma magnitud (\\( \\Delta Billetes = \\Delta Oro \\)). Esto debería elevar la tasa de interés interna, deprimir los precios nacionales, restablecer la balanza comercial y detener la fuga de reservas.",
        "doctrinal_contrast": "Frente a la Banking School (Tooke y Fullarton, quienes demostraron que al constreñir rígidamente la emisión de billetes se destruía la elasticidad del crédito necesaria para evitar pánicos bancarios transitorios)."
    },
    {
        "id": "clave_8_mckinnon_complementariedad",
        "number": 8,
        "economist_id": "mckinnon",
        "economist_name": "Ronald I. McKinnon (& Edward S. Shaw)",
        "school": "Economía del Desarrollo / Represión Financiera",
        "topic_id": "t8_represion_desarrollo",
        "topic_name": "Represión Financiera y Desarrollo Económico",
        "source_texts": [
            "Facu 66 Mc Kinnon.pdf (Money and Capital in Economic Development)"
        ],
        "title": "La Hipótesis de Complementariedad entre Dinero y Capital Físico y la Eliminación de la Represión Financiera",
        "the_key": "En las economías en desarrollo con mercados de capitales fragmentados y ausencia de crédito a largo plazo, el dinero y el capital físico no son sustitutos en el portafolio (como postulaban Keynes y Tobin), sino rigurosamente complementarios. Las tasas de interés reales positivas no deprimen la inversión sino que la potencian al facilitar la acumulación previa de saldos monetarios líquidos indispensables para financiar proyectos de inversión indivisibles.",
        "why_is_key": "Es una de las tesis más disruptivas de la teoría del desarrollo financiero. Pregunta clásica de examen: '¿Por qué para McKinnon una suba en la tasa de interés pasiva bancaria incrementa la tasa de inversión en países en desarrollo, a diferencia de los modelos neoclásicos tradicionales?'.",
        "typical_exam_trap": "Aplicar mecánicamente la regla de Tobin: \\( \\partial I / \\partial r > 0 \\) es imposible si se asume que el dinero y el capital compiten por el ahorro de los agentes. Olvidar el supuesto de 'indivisibilidad del capital' formulado por McKinnon.",
        "university_answer": "El alumno debe explicar la 'Hipótesis de Complementariedad' (o efecto conducto / conduit effect): en países en desarrollo, la gran mayoría de las unidades productivas deben autofinanciar sus inversiones de capital. Dado que la maquinaria o la tecnología son bienes indivisibles que requieren un desembolso significativo de recursos, el empresario debe ahorrar y acumular saldos monetarios reales previamente. Si el gobierno aplica 'represión financiera' fijando topes a las tasas nominales por debajo de la inflación (tasas reales fuertemente negativas), la demanda de dinero real colapsa, impidiendo la acumulación de liquidez y derrumbando la inversión. La liberación financiera y tasas reales positivas incentivan el ahorro bancario y expanden el crédito disponible para inversiones eficientes.",
        "theoretical_mechanism": "Función de demanda de dinero de McKinnon: \\( (M/P)^d = f(Y, I/Y, d - \\pi^e) \\), con la condición clave \\( \\frac{\\partial (M/P)^d}{\\partial (I/Y)} > 0 \\) (la demanda de dinero aumenta cuando aumenta la tasa de inversión respecto al producto). Función de inversión: \\( I/Y = f(r_k, d - \\pi^e) \\), donde \\( \\frac{\\partial (I/Y)}{\\partial (d - \\pi^e)} > 0 \\) mientras la tasa de interés real pasiva \\( (d - \\pi^e) \\) no supere el rendimiento medio del capital \\( r_k \\).",
        "doctrinal_contrast": "Frente al Modelo de Portafolio Neoclásico de James Tobin (donde dinero y capital son sustitutos perfectos y una tasa de interés pasiva alta encarece el costo de capital frenando la acumulación) y frente al Keynesianismo que defiende tasas de interés deprimidas artificialmente para estimular la inversión."
    },
    {
        "id": "clave_9_olivera_canavese_inflacion_estructural",
        "number": 9,
        "economist_id": "olivera_canavese",
        "economist_name": "Julio H. G. Olivera y Alfredo Canavese",
        "school": "Estructuralismo Latinoamericano / Escuela de Buenos Aires",
        "topic_id": "t3_inflacion",
        "topic_name": "Inflación Estructural y Dinero Pasivo",
        "source_texts": [
            "Facu 72 Inflación estructural Sist. Bancarios y Crediticios..pdf (Olivera y Canavese)"
        ],
        "title": "Inflación Estructural, Inflexibilidad de Precios a la Baja y el Dinero como Variable Pasiva Convalidante",
        "the_key": "La causa primaria y originaria de la inflación en economías en desarrollo es no monetaria: radica en desproporciones estructurales entre sectores (cuellos de botella en la oferta agropecuaria o externa) combinadas con asimetría o rigidez de precios a la baja en los sectores industriales. La emisión monetaria es una variable endógena y pasiva que el Banco Central se ve forzado a convalidar para evitar una recesión catastrófica y desocupación generalizada.",
        "why_is_key": "Es la doctrina de cabecera de la Cátedra para comprender la macroeconomía argentina e hispanoamericana. Los exámenes universitarios interrogan sistemáticamente: 'Si la inflación no es de origen monetario, ¿por qué la cantidad de dinero crece a la par de los precios en el modelo de Olivera?'.",
        "typical_exam_trap": "Sostener que los estructuralistas niegan la relación empírica entre dinero y precios. La genialidad analítica de Olivera reside en demostrar que el dinero acompaña rigurosamente a la inflación, pero la dirección de causalidad va del cambio de precios relativos a la convalidación monetaria pasiva, no al revés.",
        "university_answer": "El estudiante debe articular: (1) Shock estructural: aumento de la demanda urbana que choca contra una oferta agropecuaria inelástica o escasez de divisas; (2) Dispersión de precios relativos: el precio de los bienes del sector en cuello de botella debe subir relativamente (\\( P_A / P_I \\uparrow \\)); (3) Asimetría de precios (Canavese): los precios industriales no bajan ante caídas de demanda por márgenes de beneficio oligopólicos o costos laborales rígidos; (4) Suba del nivel general de precios (\\( P \\uparrow \\)); (5) El dilema del Banco Central: si el Banco Central mantuviera la oferta monetaria constante, la contracción de la liquidez real (\\( M/P \\downarrow \\)) obligaría a contraer las transacciones reales, generando desempleo y quiebras; para evitar la recesión, el Banco Central emite pasivamente. El dinero es una condición permisiva o convalidante, jamás la causa inicial.",
        "theoretical_mechanism": "Modelo formal de Olivera (1960): Sea el nivel general de precios \\( P = \\sum w_i p_i \\). Sean los excesos de demanda sectoriales \\( E_i \\). La ley de variación de precios es asimétrica: \\( \\dot{p}_i = f_i(E_i) \\) con \\( f_i'(E_i) > 0 \\) si \\( E_i > 0 \\), pero \\( \\dot{p}_i \\approx 0 \\) si \\( E_i < 0 \\). Aunque el exceso de demanda global sea nulo (\\( \\sum E_i = 0 \\)), la suma de las variaciones ponderadas es estrictamente positiva: \\( \\dot{P} = \\sum w_i \\dot{p}_i > 0 \\). La oferta de dinero se ajusta como \\( M_t = P_t \\cdot Y_t / V \\) para sostener el nivel de actividad.",
        "doctrinal_contrast": "Frente al Monetarismo de Milton Friedman (que postula que todo shock de precios relativos es absorbido con neutralidad monetaria) y frente a los modelos ortodoxtos de déficit fiscal que ignoran los cuellos de botella de la estructura productiva real."
    },
    {
        "id": "clave_10_werning_lorenzoni_inflacion_conflicto",
        "number": 10,
        "economist_id": "werning_lorenzoni",
        "economist_name": "Guido Lorenzoni e Iván Werning",
        "school": "Nuevo Keynesianismo / Macroeconomía de Frontera",
        "topic_id": "t3_inflacion",
        "topic_name": "Inflación de Ajuste vs. Inflación de Conflicto",
        "source_texts": [
            "Facu 179 Werning inflation as conflict.pdf (Inflation is Conflict)"
        ],
        "title": "Descomposición Analítica: Inflación de Ajuste (Shock Real) vs. Inflación de Conflicto (Espiral Distributiva)",
        "the_key": "La inflación contemporánea post-shocks de oferta debe descomponerse en dos fenómenos analíticamente disjuntos: la 'Inflación de Ajuste' (un salto transitorio de precios necesario para reacomodar precios relativos tras una pérdida de riqueza externa) y la 'Inflación de Conflicto' (la persistencia prolongada de alzas de precios resultante del desacuerdo distributivo no coordinado entre trabajadores y firmas, donde cada parte intenta trasladar la pérdida al otro).",
        "why_is_key": "Es el paper más reciente y sofisticado del programa (2023). En las mesas de examen se evalúa si el alumno puede superar las dicotomías simplistas (emisión vs shock de costos) y modelar formalmente la puja distributiva utilizando microfundamentos modernos de fijación de precios escalonados (Calvo / Taylor).",
        "typical_exam_trap": "Confundir la inflación transitoria de cambio de precios relativos con la inflación persistente, o creer que Werning propone que la inflación se frena simplemente con controles de precios sin un ancla monetaria y de expectativas compartidas.",
        "university_answer": "El alumno debe explicar: Cuando una economía sufre un shock adverso en los términos de intercambio o de productividad, la torta real a distribuir se achica. Si tanto los asalariados como los empresarios se niegan a asumir la reducción de su porción real (salario real \\( w/P \\) y márgenes de beneficio \\( \\mu \\)), se desata un juego no cooperativo. Los trabajadores reclaman aumentos salariales nominales para compensar la inflación pasada, y los empresarios trasladan inmediatamente el costo laboral a los precios para proteger sus márgenes. Este proceso genera una persistencia de la inflación ('inflación de conflicto') que se retroalimenta aunque el shock originario haya terminado. La política monetaria solo logra frenar la espiral generando una brecha de desempleo que discipline las demandas distributivas de las partes.",
        "theoretical_mechanism": "Modelo de Curva de Phillips con Conflicto Distributivo: Sea el salario objetivo \\( \\omega_w \\) y el margen objetivo de las empresas \\( \\omega_f \\). La suma de las aspiraciones es inconsistente con el producto real disponible: \\( \\omega_w + \\omega_f > Y \\). La inflación acumulada \\( \\pi_t \\) es función de la brecha de conflicto: \\( \\pi_t = \\beta [(\\omega_w - w_t) + (\\omega_f - \\mu_t)] + \\mathbb{E}[\\pi_{t+1}] \\). La estabilización requiere que una política de contracción reduzca el poder de mercado o que un pacto de ingresos coordine las aspiraciones.",
        "doctrinal_contrast": "Conecta la vieja literatura poskeynesiana y sociológica de la inflación de puja distributiva (Rowthorn) con los modelos neokeynesianos modernos de equilibrio general dinámico estocástico (DSGE), superando el monetarismo tradicional."
    },
    {
        "id": "clave_11_shackle_earl_incertidumbre_radical",
        "number": 11,
        "economist_id": "shackle_earl",
        "economist_name": "George L. S. Shackle (y Peter E. Earl)",
        "school": "Poskeynesianismo / Economía Conductual",
        "topic_id": "t7_expectativas_metodologia",
        "topic_name": "Incertidumbre Radical, Elección Crucial y Tiempo Histórico",
        "source_texts": [
            "Facu 86 Ex ante y ex post.pdf (Shackle & Earl)"
        ],
        "title": "Incertidumbre Radical no Probabilística versus Riesgo y el Dinero como Refugio Psicológico en el Tiempo Histórico",
        "the_key": "El futuro económico es intrínsecamente incognoscible y no creado aún; por lo tanto, no existe una distribución de probabilidad objetiva o subjetiva preexistente para asignar a los eventos venideros (diferencia fundamental entre incertidumbre radical y riesgo de Knight). En este contexto de tiempo histórico irreversible, el dinero otorga la opción vital de demorar decisiones irreversibles.",
        "why_is_key": "Examina los fundamentos metodológicos y epistemológicos de la teoría monetaria heterodoxa. Los profesores exigen que el alumno sea capaz de explicar por qué en un mundo sin riesgo ergódico probabilístico los modelos de optimización intertemporal con expectativas racionales carecen de validez científica.",
        "typical_exam_trap": "Reducir la incertidumbre a 'un riesgo con varianza muy alta'. Para Shackle y Knight, el riesgo es asegurable mediante cálculo actuarial (tirar un dado); la incertidumbre radical involucra acontecimientos únicos (elecciones cruciales) donde la acción misma del decisor destruye la configuración previa del universo económico.",
        "university_answer": "El estudiante debe destacar los conceptos cardinales de Shackle: (1) Tiempo histórico vs tiempo mecánico: el tiempo no es un eje espacial reversible; (2) La 'Sorpresa Potencial': como no se pueden enumerar todos los estados futuros de la naturaleza, el cerebro humano evalúa qué tan sorprendido estaría si un evento hipotético sucediera; (3) Elección crucial: decisiones de inversión de gran envergadura cuyos resultados son irrepetibles; (4) La función suprema del dinero: el dinero no se demanda solo por motivo transacción para aceitar intercambios, sino como un escudo protector ante la desorientación mental generada por la incertidumbre radical. La posesión de dinero preserva la libertad de maniobra del agente ante lo impredecible.",
        "theoretical_mechanism": "Crítica a la Teoría de la Utilidad Esperada: Frente a \\( \\mathbb{E}[U] = \\sum p_i U(x_i) \\), Shackle demuestra que los agentes no conocen el espacio muestral completo \\( \\Omega \\). Por tanto, la suma de probabilidades no puede sumar 1 (\\( \\sum p_i \\neq 1 \\)). Shackle propone la función de sorpresa potencial \\( y(x) \\) y el índice de foco de atención en pérdidas y ganancias potenciales extremas.",
        "doctrinal_contrast": "Frente a la Teoría de las Expectativas Racionales (Lucas, Muth, Sargent) y frente al paradigma neoclásico de Arrow-Debreu que presupone mercados de futuros completos contingentes a todos los estados del mundo posibles."
    },
    {
        "id": "clave_12_zuleta_cagan_senoreaje_hiperinflacion",
        "number": 12,
        "economist_id": "zuleta_cagan",
        "economist_name": "Hernando Zuleta G. (y Philip Cagan)",
        "school": "Economía Monetaria Aplicada",
        "topic_id": "t7_expectativas_metodologia",
        "topic_name": "Señoreaje, Impuesto Inflacionario y la Curva de Laffer",
        "source_texts": [
            "Facu 95 Señoreaje.pdf (Zuleta - Señoreaje e Impuesto Inflacionario)",
            "Facu 97 Demanda de dinero.pdf"
        ],
        "title": "Diferenciación Analítica entre Señoreaje e Impuesto Inflacionario y la Tasa de Inflación que Maximiza la Recaudación Real",
        "the_key": "El Impuesto Inflacionario es la pérdida de poder adquisitivo que sufren los tenedores de saldos monetarios reales por el alza de precios (\\( \\pi \\cdot m \\)), mientras que el Señoreaje son los recursos reales que el gobierno efectivamente captura al emitir dinero nuevo (\\( \\mu \\cdot m \\)). En equilibrio estacionario coinciden, pero en regímenes dinámicos e hiperinflaciones divergen. La curva de señoreaje tiene forma de campana (Laffer) y su máximo se alcanza en \\( \\pi^* = 1/\\alpha \\).",
        "why_is_key": "Es la demostración formal y matemática obligatoria en parciales cuantitativos de la materia. Los docentes exigen deducir paso a paso la tasa de inflación que maximiza el señoreaje utilizando la función semilogarítmica de demanda de dinero de Phillip Cagan (1956).",
        "typical_exam_trap": "Utilizar indistintamente señoreaje e impuesto inflacionario como si fueran sinónimos sin explicitar el supuesto de estado estacionario, o equivocarse en la derivada matemática olvidando que la base del impuesto (los saldos reales m) cae exponencialmente a medida que la inflación se acelera.",
        "university_answer": "El alumno debe presentar las dos ecuaciones: (1) Impuesto inflacionario: \\( TI = \\pi \\cdot (M/P) \\); (2) Señoreaje bruto: \\( S = \\frac{\\dot{M}}{P} = \\frac{\\dot{M}}{M} \\cdot \\frac{M}{P} = \\mu \\cdot m \\). En estado estacionario, donde \\( \\dot{m} = 0 \\) y el producto crece a tasa \\( g \\), \\( \\mu = \\pi + g \\). Asumiendo \\( g = 0 \\), \\( S = TI = \\pi \\cdot m(\\pi) \\). Al reemplazar la función de Cagan \\( m(\\pi) = A \\cdot e^{-\\alpha \\pi} \\), se maximiza \\( S(\\pi) = \\pi \\cdot A \\cdot e^{-\\alpha \\pi} \\). La condición de primer orden rinde inexorablemente \\( \\pi^* = \\frac{1}{\\alpha} \\). Toda emisión que lleve la inflación por encima de \\( 1/\\alpha \\) ubica a la economía en el tramo ineficiente de la Curva de Laffer monetaria, provocando caída en los ingresos reales del fisco e hiperinflación.",
        "theoretical_mechanism": "Derivación matemática rigurosa: \\( \\frac{dS}{d\\pi} = A \\cdot e^{-\\alpha \\pi} + \\pi \\cdot A \\cdot (-\\alpha) \\cdot e^{-\\alpha \\pi} = A \\cdot e^{-\\alpha \\pi} [1 - \\alpha \\pi] = 0 \\). Como \\( A \\cdot e^{-\\alpha \\pi} \\neq 0 \\), la condición de óptimo exige \\( 1 - \\alpha \\pi = 0 \\implies \\pi^* = \\frac{1}{\\alpha} \\). Condición de segundo orden: \\( \\frac{d^2S}{d\\pi^2} = -\\alpha A e^{-\\alpha \\pi} [1 - \\alpha \\pi] - \\alpha A e^{-\\alpha \\pi} = -\\alpha A e^{-\\alpha \\pi} [2 - \\alpha \\pi] < 0 \\) evaluado en \\( \\pi^* \\). El señoreaje máximo es \\( S_{max} = \\frac{A}{\\alpha \\cdot e} \\).",
        "doctrinal_contrast": "Fundamenta los modelos de hiperinflación y de estabilización fiscal de Thomas Sargent (1982, 'The Ends of Four Big Inflations') demostrando por qué los regímenes hiperinflacionarios colapsan inexorablemente cuando el gobierno intenta recaudar más allá de \\( S_{max} \\)."
    },
    {
        "id": "clave_13_harry_johnson_revolucion_economica",
        "number": 13,
        "economist_id": "harry_johnson",
        "economist_name": "Harry G. Johnson",
        "school": "Metodología y Enfoque Monetario del Balance de Pagos",
        "topic_id": "t5_crisis_fluctuaciones",
        "topic_name": "Metodología de las Revoluciones Doctrinales",
        "source_texts": [
            "Facu 64 Sist. Bancarios Harry Johnson.pdf (The Keynesian Revolution and Monetarist Counter-Revolution)"
        ],
        "title": "Las 5 Condiciones Epistemológicas y Sociológicas para el Triunfo de una Revolución Doctrinal en la Economía",
        "the_key": "Una nueva teoría económica no se impone por simple superioridad abstracta, sino cuando reúne 5 condiciones sociológicas y metodológicas indispensables que le permiten derrocar a la ortodoxia establecida en el seno de la comunidad académica y en la agenda de políticas públicas.",
        "why_is_key": "Es el texto insignia sobre epistemología de la economía de la cátedra. Los profesores evalúan si el alumno comprende cómo y por qué triunfó primero la Revolución Keynesiana sobre los Clásicos, y cómo luego la Contrarrevolución Monetarista de Friedman logró desbancar al Keynesianismo en los años 70.",
        "typical_exam_trap": "Reducir la explicación a causas coyunturales externas (como decir 'ganó Keynes por la crisis del 29 y ganó Friedman por la crisis del petróleo del 73'). Johnson demuestra que se requieren factores internos del ecosistema académico de la investigación económica.",
        "university_answer": "El alumno debe listar y justificar las 5 condiciones de Harry G. Johnson (1971): (1) Atacar una ortodoxia institucionalmente consolidada pero manifiestamente vulnerable ante acontecimientos empíricos evidentes; (2) Presentar una propuesta analítica novedosa y rebelde que simule una ruptura radical con el pasado, pero que en el fondo mantenga la suficiente continuidad metodológica para que los economistas formados en la vieja escuela no deban desaprenderlo todo; (3) Incorporar un aparato técnico o dificultad matemática que otorgue ventajas competitivas a los académicos jóvenes frente a los viejos profesores consagrados (el álgebra del IS-LM en Keynes; la econometría de series temporales y cálculo estocástico en Friedman y Lucas); (4) Ofrecer una receta o agenda de política pública atractiva y fácilmente comunicable a los gobiernos; (5) Formular un pronóstico empírico verificable que termine ocurriendo y humillando a la vieja doctrina.",
        "theoretical_mechanism": "Paralelismo histórico Johnsoniano: (a) En 1936, Keynes atacó a la ortodoxia clásica incapaz de explicar el desempleo masivo (condición 1), inventó la función consumo y el multiplicador manteniendo el equilibrio marshalliano (condición 2), introdujo la formalización agregada (condición 3), ofreció el gasto público anticíclico (condición 4) y predijo la persistencia del estancamiento sin intervención (condición 5). (b) En los 70, Friedman atacó la Curva de Phillips keynesiana que no podía explicar la estanflación (condición 1), reformuló la teoría cuantitativa sin rechazar la función de demanda de dinero (condición 2), usó regresiones estadísticas masivas (condición 3), ofreció la regla del k% (condición 4) y predijo con precisión que expandir el dinero causaría inflación acelerada sin bajar el desempleo a largo plazo (condición 5).",
        "doctrinal_contrast": "Aplica la teoría de las revoluciones científicas de Thomas Kuhn (paradigmas y anomalías) a la ciencia económica, analizando el choque entre Cambridge (Keynes) y Chicago (Friedman)."
    },
    {
        "id": "clave_14_clasicos_poskeynesianos_neutralidad",
        "number": 14,
        "economist_id": "clasicos_poskeynesianos",
        "economist_name": "Clásicos vs. Poskeynesianos",
        "school": "Debate Doctrinal Integrador (Fisher/Pigou vs. Kaldor/Moore/Wray)",
        "topic_id": "t2_demanda_dinero",
        "topic_name": "Neutralidad y Causalidad de la Oferta Monetaria",
        "source_texts": [
            "Facu 97 Demanda de dinero.pdf",
            "Facu 174 Banking School.pdf",
            "Facu 108 De Keynes a Lucas.pdf"
        ],
        "title": "La Gran Controversia Doctrinal: Dicotomía Clásica y Neutralidad vs. Dinero Endógeno de Circuito ('Loans Create Deposits')",
        "the_key": "Para el paradigma Clásico/Monetarista, el dinero es exógeno (determinado por la oferta de la autoridad monetaria), actúa como un velo neutral a largo plazo y la causalidad macroeconómica fluye de la masa monetaria hacia el nivel de precios. Para el paradigma Poskeynesiano/Circuito Monetario, el dinero es estrictamente endógeno, creado por los bancos privados al emitir crédito productivo ('los préstamos crean los depósitos'), la causalidad fluye de los costos de producción y demanda de crédito a la cantidad de dinero, y el dinero NUNCA es neutral.",
        "why_is_key": "Es la pregunta integradora por excelencia de los exámenes finales de la cátedra de Sistemas Bancarios y Teoría Monetaria. Sintetiza la divisoria de aguas de toda la materia y permite corroborar si el estudiante puede articular simultáneamente los 8 ejes temáticos del programa.",
        "typical_exam_trap": "Tratar el multiplicador bancario tradicional (donde el Banco Central inyecta base monetaria y los bancos 'multiplican' mecánicamente) como una verdad científica universal incuestionable. Para los poskeynesianos, esa es una fábula contable que confunde la causalidad de los hechos.",
        "university_answer": "El alumno debe estructurar un cuadro comparativo riguroso: (1) Causalidad de la oferta de dinero: Clásica/Monetarista: Base monetaria exógena \\( B \\to \\) Depósitos \\( D \\to \\) Crédito \\( C \\). Poskeynesiana: Demanda de crédito solvente de empresas para pagar masa salarial \\( \\to \\) Los bancos extienden préstamos creando depósitos de la nada ('ex nihilo') \\( \\to \\) El Banco Central convalida como prestamista de última instancia inyectando las reservas requeridas para no quebrar el sistema de pagos fijando la tasa de interés interbancaria. (2) Neutralidad: Clásica: Dicotomía clásica, el dinero no altera la asignación de recursos reales a largo plazo (solo precios nominales). Poskeynesiana: La producción capitalista toma tiempo y se realiza bajo contratos monetarios denominados en dinero de curso legal; la liquidez y las deudas condicionan permanentemente las decisiones de acumulación real.",
        "theoretical_mechanism": "Formalización de la secuencia del Circuito Monetario (Graziani, Kaldor, Wray): Momento 1: Financiación inicial del proceso de producción: Empresas solicitan crédito a bancos para pagar salarios nominales \\( W \\cdot L \\). Los bancos otorgan el crédito acreditando cuentas corrientes (\\( \\Delta \\text{Activo}_{\\text{banco}} = \\text{Préstamo} \\), \\( \\Delta \\text{Pasivo}_{\\text{banco}} = \\text{Depósito} \\)). Momento 2: Consumo e Inversión: Los trabajadores gastan su salario en bienes de consumo producidos por las firmas. Momento 3: Cierre del circuito: Las firmas recaudan los ingresos por ventas y cancelan el préstamo original con el banco, destruyendo el dinero previamente creado. Por ende, la masa monetaria \\( M \\) se expande y contrae endógenamente al compás de la producción y el crédito.",
        "doctrinal_contrast": "Representa el antagonismo doctrinal irreconciliable de la macroeconomía contemporánea entre la Escuela Ortodoxa (Clásicos, Monetaristas, Nueva Macroeconomía Clásica) y la Escuela Heterodoxa (Poskeynesianos, Escuela del Circuito, Teoría Monetaria Moderna)."
    }
]

def main():
    print("Iniciando actualización de la base de datos con las 14 Claves Maestras para el Examen...")

    # Load existing static_data.json
    with open("static_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    # Insert exam_keys
    data["exam_keys"] = EXAM_KEYS
    data["metadata"]["total_exam_keys"] = len(EXAM_KEYS)

    # Save to static_data.json and static/static_data.json
    with open("static_data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    with open("static/static_data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    # Save to data.js and static/data.js
    js_content = f"window.BANKING_DATA = {json.dumps(data, ensure_ascii=False, indent=2)};"
    with open("data.js", "w", encoding="utf-8") as f:
        f.write(js_content)

    with open("static/data.js", "w", encoding="utf-8") as f:
        f.write(js_content)

    print(f"Éxito: Se generaron e inyectaron las {len(EXAM_KEYS)} Claves de Examen en root y static!")

if __name__ == "__main__":
    main()


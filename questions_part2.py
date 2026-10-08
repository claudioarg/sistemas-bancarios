# -*- coding: utf-8 -*-
"""
questions_part2.py - Questions for:
- Lorenzoni & Werning (20)
- Shackle & Earl (20)
- Zuleta & Cagan (20)
- Harry Johnson (20)
- Clásicos y Poskeynesianos (Fisher, Pigou, Baumol, Tobin) (20)
Total: 100 questions.
"""

bank_part2 = {}

# -------------------------------------------------------------
# 9. GUIDO LORENZONI E IVÁN WERNING (20 preguntas)
# -------------------------------------------------------------
bank_part2["werning_lorenzoni"] = [
    {
        "id": "werning_1",
        "question": "¿Cuál es la provocadora demostración teórica que realizan Guido Lorenzoni e Iván Werning en 'Inflation is Conflict' (NBER, 2023)?",
        "options": [
            "Que la inflación solo puede existir si el Banco Central emite billetes de curso forzoso.",
            "Que la inflación florece, persiste y se perpetúa en un modelo analítico estilizado donde NO EXISTE dinero, crédito, tasas de interés, producción ni desempleo.",
            "Que la inflación desaparece por completo cuando se eliminan los sindicatos laborales.",
            "Que el tipo de cambio fijo es matemáticamente imposible de sostener en economías abiertas."
        ],
        "correct_index": 1,
        "explanation": "Aporte epistemológico cumbre: aíslan deliberadamente el dinero y los mercados financieros para demostrar que la fuerza motriz generadora y persistente de la inflación es puramente el conflicto distributivo entre agentes."
    },
    {
        "id": "werning_2",
        "question": "¿Cuál es la definición esencial de la inflación según Lorenzoni y Werning?",
        "options": [
            "La pérdida de respaldo en lingotes de oro de la moneda de curso legal.",
            "La manifestación macroeconómica visible del desacuerdo o conflicto distributivo entre los agentes económicos por la apropiación de la torta productiva disponible.",
            "Un error técnico de cálculo en los índices de precios del Instituto Nacional de Estadística.",
            "El resultado inevitable del crecimiento acelerado de la productividad industrial."
        ],
        "correct_index": 1,
        "explanation": "La tesis central es que 'Inflation is Conflict': la inflación es el síntoma de que las pretensiones de ingresos de los distintos sectores sociales son mutuamente incompatibles."
    },
    {
        "id": "werning_3",
        "question": "¿En qué consiste la 'Incompatibilidad de Pretensiones Distributivas' formulada por Lorenzoni y Werning?",
        "options": [
            "En la discrepancia entre las exportaciones e importaciones del comercio exterior.",
            "En que la suma del salario real deseado por los trabajadores (w/p)^d y el margen de beneficio o markup deseado por las empresas (P/W)^d supera el 100% del ingreso nacional disponible.",
            "En la negativa de los jubilados a pagar el impuesto a las ganancias.",
            "En el desacuerdo entre el Poder Ejecutivo y el Banco Central sobre la tasa de interés."
        ],
        "correct_index": 1,
        "explanation": "Si los trabajadores exigen un salario real del 60% de la torta y las empresas exigen un margen de beneficio del 55%, las demandas suman 115%. Como la torta es el 100%, la incompatibilidad se traduce en aumentos sucesivos de precios."
    },
    {
        "id": "werning_4",
        "question": "En el modelo de Lorenzoni y Werning, ¿por qué la puja distributiva genera una tasa positiva y continua de inflación en lugar de un salto de precios de una sola vez?",
        "options": [
            "Porque el Banco Central duplica la base monetaria todos los meses.",
            "Debido a la fijación escalonada y asincrónica de precios y salarios en el tiempo (tipo contratos de Calvo).",
            "Porque los trabajadores demandan cobrar sus sueldos en monedas de oro.",
            "Porque las empresas quiebran automáticamente cada dos trimestres."
        ],
        "correct_index": 1,
        "explanation": "Los agentes no pueden renegociar precios y salarios al unísono en cada segundo; ajustan de manera escalonada en turnos alternados. Cuando un sector ajusta, descoloca al otro, desatando una espiral continua en el tiempo."
    },
    {
        "id": "werning_5",
        "question": "¿Cómo opera la 'Espiral Salarios-Precios' (Wage-Price Spiral) descrita en el artículo?",
        "options": [
            "Los precios bajan $\\rightarrow$ los salarios suben $\\rightarrow$ la inversión colapsa.",
            "Trabajadores suben salarios nominales para recuperar salario real $\\rightarrow$ empresas suben precios para defender margen $\\rightarrow$ salario real cae de nuevo $\\rightarrow$ se reinicia la espiral.",
            "El gobierno congela salarios y precios a perpetuidad mediante decreto administrativo.",
            "Los empresarios pagan salarios en dólares y venden sus productos en moneda nacional."
        ],
        "correct_index": 1,
        "explanation": "Dinámica de la espiral: cada grupo intenta defender su tajada en su turno de fijación. En términos reales el conflicto termina en un empate frustrado, pero como subproducto engendra inflación continua en todas las variables nominales."
    },
    {
        "id": "werning_6",
        "question": "¿Cuál es la distinción analítica fundamental que introducen Lorenzoni y Werning entre los dos tipos de inflación?",
        "options": [
            "Inflación buena e inflación mala.",
            "Inflación de Ajuste (Adjustment Inflation) vs Inflación de Conflicto (Conflict Inflation).",
            "Inflación minorista vs Inflación mayorista.",
            "Inflación estacional vs Inflación de tendencia."
        ],
        "correct_index": 1,
        "explanation": "Pilar de examen: 1) Inflación de Ajuste: cambio de precios transitorio derivado del reacomodamiento eficiente de precios relativos tras un shock; 2) Inflación de Conflicto: inflación persistente alimentada por la lucha distributiva asincrónica."
    },
    {
        "id": "werning_7",
        "question": "¿Qué propiedades caracterizan a la 'Inflación de Ajuste' (Adjustment Inflation)?",
        "options": [
            "Es hiperinflacionaria, dura décadas y destruye la moneda nacional.",
            "Es transitoria, de magnitud acotada, refleja el cambio eficiente de precios relativos ante un shock y se extingue por sí sola sin persistencia.",
            "Requiere que el desempleo suba al 30% para poder frenarse.",
            "Es causada exclusivamente por la emisión de títulos de deuda pública soberana."
        ],
        "correct_index": 1,
        "explanation": "Cuando ocurre un shock (por ejemplo, sube la energía), los precios relativos deben reacomodarse. Este ajuste eleva transitoriamente el índice de precios, pero una vez completado el reacomodamiento, la inflación cesa sola."
    },
    {
        "id": "werning_8",
        "question": "¿Por qué la 'Inflación de Conflicto' (Conflict Inflation) es la verdadera responsable de la persistencia inflacionaria?",
        "options": [
            "Porque los bancos comerciales especulan en los mercados de divisas.",
            "Porque ante un shock que reduce la torta real, los agentes se niegan a absorber la pérdida y desatan una pugna continua de aumentos escalonados de salarios y markups.",
            "Porque el gobierno suspende el pago de la deuda pública externa.",
            "Porque la productividad del trabajo se multiplica por diez."
        ],
        "correct_index": 1,
        "explanation": "Si un shock negativo encarece la energía, la torta interna se achica. Si trabajadores y firmas intentan mantener intactos sus ingresos reales previos, la incompatibilidad se agrava y la espiral salarios-precios se vuelve interminable."
    },
    {
        "id": "werning_9",
        "question": "En el marco de Werning y Lorenzoni, ¿por qué los shocks de oferta negativos (como el shock energético o cuellos de botella post-COVID) aceleran la inflación?",
        "options": [
            "Porque incrementan la preferencia por billetes de baja denominación del público.",
            "Porque reducen el tamaño de la torta productiva real disponible, haciendo que las pretensiones previas de salarios y beneficios choquen con mayor violencia.",
            "Porque obligan a cerrar las cuentas corrientes bancarias.",
            "Porque aumentan automáticamente la tasa de interés natural de la economía."
        ],
        "correct_index": 1,
        "explanation": "Al haber menos torta real para repartir tras el shock, las aspiraciones de ingresos de empresas y asalariados son aún más incompatibles matemáticamente, intensificando la puja y disparando la inflación de conflicto."
    },
    {
        "id": "werning_10",
        "question": "¿Cómo reinterpretan Lorenzoni y Werning el canal de transmisión de la política monetaria contractiva (suba de tasas de interés de la Fed o bancos centrales)?",
        "options": [
            "La suba de tasas absorbe físicamente los billetes que circulan en la calle mediante imanes magnéticos.",
            "La política monetaria reduce la inflación porque enfría la demanda agregada y eleva el desempleo, forzando un 'armisticio obligatorio' en el conflicto distributivo.",
            "La suba de tasas convence éticamente a los empresarios de reducir voluntariamente sus precios.",
            "La política monetaria actúa incrementando la productividad física de las fábricas."
        ],
        "correct_index": 1,
        "explanation": "Desmitificación del canal monetario: subir tasas reduce el gasto deprimie las ventas (lo que debilita el poder de fijación de precios y markups de las firmas) y eleva el desempleo (debilitando el poder de reclamo salarial), imponiendo una tregua forzosa."
    },
    {
        "id": "werning_11",
        "question": "¿Qué efecto tiene un aumento del desempleo sobre la pugna distributiva en el modelo de Lorenzoni y Werning?",
        "options": [
            "Aumenta la agresividad de las demandas salariales de los sindicatos.",
            "Debilita el poder de negociación de los trabajadores, forzándolos a moderar sus pretensiones salariales nominales y aceptando una menor tajada de la torta real.",
            "Provoca la quiebra inmediata de las empresas productoras de alimentos.",
            "Elimina la necesidad de calcular el índice de precios al consumidor."
        ],
        "correct_index": 1,
        "explanation": "Con mayor desempleo, el miedo a perder el puesto frena los reclamos salariales; la suma de aspiraciones de trabajadores y empresas vuelve a converger hacia el 100% de la torta, deteniendo la espiral."
    },
    {
        "id": "werning_12",
        "question": "¿Qué puente doctrinal construyen Lorenzoni y Werning entre dos tradiciones históricamente enfrentadas?",
        "options": [
            "Entre la Fisiocracia de Quesnay y el Mercantilismo británico.",
            "Entre la tradición postkeynesiana/estructuralista del conflicto social (Rowthorn, 1977) y los modelos macroeconómicos contemporáneos Nuevo Keynesianos microfundamentados con fijación de precios escalonada.",
            "Entre la Escuela Austríaca de Mises y el Marxismo soviético.",
            "Entre el Plan Chicago del 100% de reservas y la banca libre escocesa."
        ],
        "correct_index": 1,
        "explanation": "Logro analítico: formalizan matemáticamente la vieja intuición poskeynesiana de la puja distributiva de Bob Rowthorn dentro de un marco analítico moderno riguroso aceptado por la corriente principal."
    },
    {
        "id": "werning_13",
        "question": "¿Qué papel juega el 'margen de beneficio' o markup de las firmas en la teoría de Lorenzoni y Werning?",
        "options": [
            "Es una constante pasiva fijada por el gobierno federal en el 5% anual.",
            "Es una variable activa donde las empresas defienden su rentabilidad subiendo precios ante cualquier incremento en los costos salariales o de insumos.",
            "Es un subsidio tributario que reciben los accionistas bancarios.",
            "Desaparece en cuanto la economía entra en recesión."
        ],
        "correct_index": 1,
        "explanation": "Las empresas no absorben pasivamente los aumentos salariales: los trasladan a los precios para proteger su margen de ganancia deseado, retroalimentando la espiral."
    },
    {
        "id": "werning_14",
        "question": "¿Por qué Lorenzoni y Werning señalan que la política monetaria contractiva es una herramienta costosa y dolorosa para frenar la inflación?",
        "options": [
            "Porque imprimir billetes a tasas altas gasta demasiada tinta.",
            "Porque para detener la espiral distributiva la política monetaria debe destruir actividad económica real y generar desempleo forzoso hasta quebrar las demandas de los agentes.",
            "Porque encarece el costo de las elecciones legislativas.",
            "Porque el Banco Central debe cerrar sucursales en el interior del país."
        ],
        "correct_index": 1,
        "explanation": "La tasa de interés no ataca la causa del conflicto; solo impone una tregua forzosa destruyendo empleo y ventas para que las partes bajen sus pretensiones por la fuerza de la recesión."
    },
    {
        "id": "werning_15",
        "question": "¿Qué alternativa o complemento de política económica sugieren los modelos de conflicto distributivo para reducir el costo en desempleo de la desinflación?",
        "options": [
            "La prohibición de importar petróleo y gas natural.",
            "Políticas de ingresos, acuerdos tripartitos o pactos sociales coordinados que congelen o escalonen ordenadamente precios y salarios para resolver la incompatibilidad sin recesión masiva.",
            "La disolución de los tribunales laborales.",
            "La entrega de subsidios directos a las empresas monopolistas."
        ],
        "correct_index": 1,
        "explanation": "Si trabajadores y empresas coordinan simultáneamente moderar sus márgenes y salarios mediante un pacto social creíble, la inflación de conflicto puede frenarse sin necesidad de provocar desempleo masivo."
    },
    {
        "id": "werning_16",
        "question": "¿Cómo contrasta la tesis de Lorenzoni y Werning ('Inflation is Conflict') con la clásica frase monetarista de Milton Friedman?",
        "options": [
            "Coinciden plenamente en que la emisión de billetes es la única causa de la inflación.",
            "Friedman afirma que la inflación es siempre un fenómeno puramente monetario; Lorenzoni y Werning demuestran que la inflación surge del desacuerdo distributivo real, siendo el dinero totalmente prescindible para su existencia.",
            "Ambos sostienen que la inflación es provocada por los aranceles de importación.",
            "Lorenzoni y Werning afirman que la inflación solo ocurre en economías con moneda metálica pura."
        ],
        "correct_index": 1,
        "explanation": "Confrontación nodal de examen: frente al dogma monetarista de que el dinero causa todo, Lorenzoni y Werning prueban que la inflación es el subproducto de una lucha distributiva en la economía real, incluso en ausencia de dinero."
    },
    {
        "id": "werning_17",
        "question": "¿Qué ocurre con las expectativas de inflación en el modelo de Lorenzoni y Werning?",
        "options": [
            "Son siempre iguales a cero en todos los períodos.",
            "Los agentes anticipan racionalmente que los demás sectores subirán sus precios y salarios en el futuro, incorporando esa previsión en sus propios aumentos presentes y consolidando la persistencia.",
            "Son gobernadas exclusivamente por las fases de la luna.",
            "Se corrigen mediante un sorteo trimestral organizado por el Congreso."
        ],
        "correct_index": 1,
        "explanation": "La previsión de que la otra parte continuará aumentando precios induce a cada agente a exigir aumentos preventivos mayores en su propio turno para proteger su poder de compra futuro."
    },
    {
        "id": "werning_18",
        "question": "En el modelo sin dinero de la primera sección de 'Inflation is Conflict', ¿cómo se liquidan las transacciones de los bienes?",
        "options": [
            "Mediante pagarés en criptomonedas no reguladas.",
            "Como un intercambio walrasiano descentralizado de precios relativos escalonados donde los bienes se fijan en términos de una unidad de cuenta abstracta.",
            "Mediante el trueque físico de ganado vacuno por trigo.",
            "A través de tarjetas de crédito emitidas por bancos de inversión."
        ],
        "correct_index": 1,
        "explanation": "Utilizan una unidad de cuenta abstracta para demostrar con elegancia matemática que no se necesita masa monetaria física para que la dinámica de precios nominales exhiba una espiral inflacionaria persistente."
    },
    {
        "id": "werning_19",
        "question": "¿Qué relación existe entre la 'Inflación de Conflicto' de Lorenzoni y Werning y la inflación estructural del latinoamericanismo (Olivera-Canavese)?",
        "options": [
            "No guardan ningún punto de contacto teórico.",
            "Ambas corrientes identifican a la pugna distributiva y a las rigideces nominales como el motor de propagación del alza de precios, aunque Werning y Lorenzoni la formalizan con microfundamentos de optimización intertemporal.",
            "Olivera sostenía que la inflación era monetarista y Werning que era fiscalista.",
            "Ambas fueron formuladas por encargo directo del Banco de Inglaterra en el siglo XIX."
        ],
        "correct_index": 1,
        "explanation": "Afinidad doctrinal profunda: tanto los estructuralistas de la CEPAL como Lorenzoni y Werning ubican la raíz de la inflación en la puja por el ingreso entre clases y sectores tras perturbaciones en la economía real."
    },
    {
        "id": "werning_20",
        "question": "¿Cuál es la lección central de 'Inflation is Conflict' para los bancos centrales en épocas de shocks de oferta globales?",
        "options": [
            "Que deben emitir dinero a una tasa fija del 3% anual según la regla k% de Friedman.",
            "Que no deben confundir la inflación transitoria de ajuste de precios relativos con la inflación persistente de conflicto, evitando sobrereaccionar con subas brutales de tasas que generen desempleo innecesario ante ajustes eficientes.",
            "Que deben prohibir el funcionamiento de los sindicatos de trabajadores.",
            "Que deben vender todas sus reservas de oro en el mercado internacional."
        ],
        "correct_index": 1,
        "explanation": "Lección de política: la autoridad monetaria debe permitir que la inflación de ajuste ocurra para que los precios relativos se acomoden; solo debe intervenir enérgicamente si el shock degenera en una espiral desanclada de conflicto distributivo."
    }
]

# -------------------------------------------------------------
# 10. GEORGE L. S. SHACKLE (Y PETER E. EARL) (20 preguntas)
# -------------------------------------------------------------
bank_part2["shackle_earl"] = [
    {
        "id": "shackle_1",
        "question": "¿Cuál es la crítica epistemológica demoledora que formula G. L. S. Shackle a la teoría de la elección neoclásica tradicional?",
        "options": [
            "Que los modelos matemáticos no utilizan suficientes variables macroeconómicas agregadas.",
            "Que asume falsamente que el futuro económico es un espacio probabilístico calculable mediante distribuciones objetivas de riesgo, cuando en realidad es radicalmente incierto y aún no ha sido creado.",
            "Que los economistas no consideran el valor de cambio del oro físico.",
            "Que la teoría neoclásica otorga demasiada importancia a la psicología de los consumidores."
        ],
        "correct_index": 1,
        "explanation": "Para Shackle, las decisiones de inversión económica son experimentos únicos e irrepetibles en un tiempo histórico irreversible. Como el futuro no existe, es imposible calcular distribuciones de probabilidad objetivas."
    },
    {
        "id": "shackle_2",
        "question": "En el marco de Shackle rescatado por Peter E. Earl (2018), ¿cómo se define el concepto de 'Incertidumbre Radical' frente al 'Riesgo'?",
        "options": [
            "El riesgo se aplica a las quiebras bancarias y la incertidumbre a las catástrofes naturales.",
            "El riesgo admite frecuencias estadísticas repetibles (ruleta, seguros actuariales); en la incertidumbre radical las decisiones son únicas y los resultados posibles son imaginados por la mente humana sin base probabilística.",
            "El riesgo es una variable microeconómica y la incertidumbre es macroeconómica.",
            "Son conceptos idénticos que se miden con la varianza matemática de una distribución normal."
        ],
        "correct_index": 1,
        "explanation": "Diferencia insalvable: el riesgo pertenece al mundo de eventos reproducibles en laboratorios o casinos. La inversión capitalista es un experimento irrepetible donde la mente crea hipótesis imaginadas."
    },
    {
        "id": "shackle_3",
        "question": "¿Qué significa la concepción shackleana del 'Tiempo Histórico Irreversible' frente al tiempo de la física clásica?",
        "options": [
            "Que los relojes económicos deben atrasarse una hora en los meses de invierno.",
            "Que el tiempo económico avanza en una sola dirección; el pasado es memoria inmutable y el futuro es vacío, no pudiendo 'deshacerse' una decisión de inversión equivocada como en los modelos estáticos atemporales.",
            "Que la historia económica se repite de manera idéntica y circular cada cincuenta años.",
            "Que las transacciones bursátiles tardan varias semanas en liquidarse físicamente."
        ],
        "correct_index": 1,
        "explanation": "El tiempo histórico es irreversible: comprometer capital en una fábrica crea una realidad nueva e irrevocable; no se puede volver atrás ni aplicar el equilibrio estático reversible de la física mecánica."
    },
    {
        "id": "shackle_4",
        "question": "¿En qué consiste el concepto del 'Momento del Presente' (Moment-in-Being) en la teoría de la decisión de Shackle?",
        "options": [
            "El instante exacto en que suena la campana de apertura de la Bolsa de Londres.",
            "La idea de que la elección humana solo existe en el instante presente ex-ante basada en la imaginación y las expectativas subjetivas; el resultado ex-post es un hecho histórico inerte.",
            "La duración máxima permitida para los préstamos a la vista en los bancos comerciales.",
            "El tiempo que tarda una orden de compra en ejecutarse mediante sistemas informáticos."
        ],
        "correct_index": 1,
        "explanation": "Toda elección ocurre en el 'ahora' (moment-in-being). El inversor compara escenarios rivales imaginados en su mente en el presente; una vez transcurrido el tiempo, el resultado es historia fija y no elección."
    },
    {
        "id": "shackle_5",
        "question": "¿Cuál es la función suprema que cumple el DINERO en la teoría económica de Shackle?",
        "options": [
            "Un simple lubricante mecánico para acelerar el trueque de bienes.",
            "Un escudo psicológico que otorga 'inmunidad contra el compromiso en un mundo incierto', preservando abiertas todas las opciones futuras frente a lo desconocido.",
            "Un activo de especulación bursátil para obtener ganancias de capital a corto plazo.",
            "Un instrumento coercitivo del Estado para cobrar impuestos tributarios ordinarios."
        ],
        "correct_index": 1,
        "explanation": "Definición célebre: demandar dinero es la respuesta instintiva para no atar los recursos a compromisos físicos irrevocables en un mundo cuyo destino no puede calcularse. Otorga 'inmunidad contra el compromiso'."
    },
    {
        "id": "shackle_6",
        "question": "¿Cómo fundamenta Shackle desde la psicología introspectiva la 'Preferencia por la Liquidez' de John Maynard Keynes?",
        "options": [
            "Afirma que la demanda de liquidez es el resultado de un cálculo matemático de optimización intertemporal de segundo orden.",
            "Demuestra que retener saldos líquidos alivia la angustia real y el estrés emocional de los empresarios ante la ignorancia del porvenir.",
            "Sostiene que el público demanda dinero exclusivamente para evadir controles policiales.",
            "Argumenta que la preferencia por la liquidez es un hábito irracional que debe ser castigado por ley."
        ],
        "correct_index": 1,
        "explanation": "Shackle dota a la teoría keynesiana de fundamentos psicológicos introspectivos: la preferencia por la liquidez es un mecanismo de defensa mental contra la vulnerabilidad existencial ante la ignorancia del futuro."
    },
    {
        "id": "shackle_7",
        "question": "¿En qué consiste la 'Teoría de la Sorpresa Potencial' (Potential Surprise Theory) ideada por Shackle como alternativa a la probabilidad?",
        "options": [
            "En medir el asombro de los economistas cuando fracasan sus predicciones del PBI.",
            "En asignar a cada desenlace imaginado un grado subjetivo de sorpresa potencial (y), que va desde cero (suceso perfectamente creíble) hasta sorpresa máxima (evento inverosímil o inconcebible).",
            "En calcular la probabilidad matemática acumulada de eventos que superan el 95% de confianza.",
            "En evaluar el impacto de los descubrimientos tecnológicos en la producción minera."
        ],
        "correct_index": 1,
        "explanation": "Al no haber probabilidades numéricas objetivas, los agentes asignan grados de sorpresa potencial a sus hipótesis mentales: cuanto más plausible es un resultado, menor sorpresa generaría su concreción (y = 0)."
    },
    {
        "id": "shackle_8",
        "question": "¿Qué son los 'Focos de Decisión' (Focus Outcomes) en la teoría de la elección de Shackle?",
        "options": [
            "Las ciudades donde se concentran las sedes centrales de los bancos multinacionales.",
            "Los dos puntos extremos que capturan la atención del decisor: la máxima ganancia concebible y la peor pérdida concebible que no generarían sorpresa potencial.",
            "Los objetivos anuales de recaudación impositiva fijados por el Ministerio de Economía.",
            "Las tasas de interés de equilibrio entre el mercado de bonos y el mercado de acciones."
        ],
        "correct_index": 1,
        "explanation": "El decisor no evalúa una curva continua de densidades. Su atención se polariza en dos focos mentales: el foco de ganancia (el mejor éxito creíble) y el foco de pérdida (el peor desastre creíble), decidiendo en base a este contraste."
    },
    {
        "id": "shackle_9",
        "question": "¿Cómo se originan las crisis y recesiones económicas en la concepción de Shackle?",
        "options": [
            "Por un exceso de regulación estatal en los mercados de trabajo.",
            "Cuando un acontecimiento imprevisto de alta 'sorpresa potencial' pulveriza las convenciones y escenarios mentales vigentes, desatando pánico, parálisis inversora y huida a la liquidez.",
            "Por la quiebra simultánea de los productores agrícolas de granos.",
            "Por el aumento del salario mínimo legal por encima de la productividad marginal."
        ],
        "correct_index": 1,
        "explanation": "Génesis de la crisis: la actividad descansa en convenciones precarias. Cuando ocurre un hecho traumático que nadie imaginó (alta sorpresa), las certezas mentales se derrumban, paralizando la inversión."
    },
    {
        "id": "shackle_10",
        "question": "¿Por qué Shackle es sumamente escéptico frente a la macroeconometría y los modelos de predicción cuantitativa?",
        "options": [
            "Porque los modelos no utilizan computadoras de última generación.",
            "Porque la economía está impulsada por la imaginación humana creadora y pensamientos que aún no han ocurrido; los datos estadísticos pasados son historia inerte que no contiene las ideas futuras.",
            "Porque los econometristas cobran honorarios excesivamente elevados por sus asesorías.",
            "Porque el producto bruto interno no puede medirse en unidades monetarias constantes."
        ],
        "correct_index": 1,
        "explanation": "El futuro no está esperando ser descubierto como un planeta en el cielo; el futuro es creado continuamente por decisiones humanas novedosas. Por ende, extrapolar series históricas hacia adelante es científicamente falaz."
    },
    {
        "id": "shackle_11",
        "question": "¿De qué dos colosos del pensamiento económico del siglo XX fue discípulo simultáneo George L. S. Shackle?",
        "options": [
            "De Karl Marx y Friedrich Engels.",
            "De John Maynard Keynes en Cambridge y Friedrich A. von Hayek en la London School of Economics (LSE).",
            "De Milton Friedman en Chicago e Irving Fisher en Yale.",
            "De Paul Samuelson en el MIT y Robert Lucas en Chicago."
        ],
        "correct_index": 1,
        "explanation": "Shackle integró la visión de la incertidumbre subjetiva y el dinero de Keynes con la concepción del tiempo, el conocimiento disperso y el orden espontáneo de Hayek, forjando su teoría de la imaginación."
    },
    {
        "id": "shackle_12",
        "question": "¿Qué relación existe entre la obra de Shackle y la moderna 'Economía del Comportamiento' (Behavioral Economics)?",
        "options": [
            "Shackle se opuso tenazmente a cualquier enfoque que mencionara la psicología humana.",
            "Shackle fue un precursor visionario de la racionalidad acotada de Herbert Simon y de la Teoría de las Perspectivas de Daniel Kahneman y Amos Tversky.",
            "Ambas corrientes sostienen que los agentes económicos tienen previsión perfecta intertemporal.",
            "La Economía del Comportamiento demostró que los focos de decisión de Shackle eran errores contables."
        ],
        "correct_index": 1,
        "explanation": "Peter Earl demuestra que los conceptos de Shackle (atención selectiva, puntos focales de pérdida, heurísticas y descarte de probabilidades numéricas) anticiparon en varias décadas los aportes de Kahneman y Tversky."
    },
    {
        "id": "shackle_13",
        "question": "¿Por qué Shackle rechaza categóricamente la Hipótesis de Expectativas Racionales de Robert Lucas?",
        "options": [
            "Porque Lucas no consideraba la existencia de los bancos comerciales.",
            "Porque asumir que los agentes conocen la 'verdadera distribución de probabilidad objetiva' del futuro niega la esencia misma de la libertad, la creatividad y la ignorancia genuina del ser humano.",
            "Porque las expectativas racionales exigen el retorno al patrón oro internacional.",
            "Porque Lucas utilizaba modelos matemáticos de optimización dinámica."
        ],
        "correct_index": 1,
        "explanation": "Para Shackle, postular que el futuro ya está determinado estocásticamente en un modelo conocido convierte a los seres humanos en autómatas preprogramados, anulando la imaginación y la elección real."
    },
    {
        "id": "shackle_14",
        "question": "¿Cuál es la crítica que formula Shackle al instrumentalismo del 'como si' de Milton Friedman?",
        "options": [
            "Afirma que Friedman utilizaba datos estadísticos de mala calidad.",
            "Sostiene que ignorar intencionalmente los procesos mentales reales de deliberación y tratar a los agentes 'como si' fueran máquinas predictivas destruye la comprensión real de la acción humana bajo incertidumbre.",
            "Considera que Friedman era un keynesiano encubierto.",
            "Afirma que los supuestos de una teoría deben ser aprobados por plebiscito popular."
        ],
        "correct_index": 1,
        "explanation": "Shackle exige realismo psicológico e introspectivo: no se puede entender el colapso de la inversión y la demanda de dinero ignorando la angustia, la duda y el proceso creativo que ocurre en la mente del decisor."
    },
    {
        "id": "shackle_15",
        "question": "¿Cómo concibe Shackle la actividad de los banqueros comerciales al otorgar préstamos?",
        "options": [
            "Como una rutina matemática exenta de cualquier riesgo crediticio.",
            "Como apuestas audaces en un tiempo histórico irreversible, donde cada crédito financia proyectos futuros que aún no existen y cuyos desenlaces no pueden calcularse con tablas actuariales.",
            "Como una función administrativa delegada por el Ministerio de Hacienda.",
            "Como operaciones de permuta física de bienes de consumo por bienes de capital."
        ],
        "correct_index": 1,
        "explanation": "Los bancos no son computadoras que calculan probabilidades; son evaluadores subjetivos que apuestan por visiones de futuro de empresarios. Si el clima de negocios se ensombrece, el crédito se paraliza por miedo a lo desconocido."
    },
    {
        "id": "shackle_16",
        "question": "¿Qué es la 'Gama de Resultados Creíbles' (Range of Plausible Outcomes) en el esquema de Shackle?",
        "options": [
            "El intervalo de precios fijado por la ley de abastecimiento estatal.",
            "El conjunto de hipótesis sobre el futuro que un individuo puede concebir en su mente sin que le generen una sensación inmediata de sorpresa potencial o absurdo.",
            "Las tasas de inflación proyectadas por el Fondo Monetario Internacional a diez años.",
            "El porcentaje de votantes indecisos en una elección presidencial."
        ],
        "correct_index": 1,
        "explanation": "El decisor delimita mentalmente lo creíble de lo imposible: descarta los desenlaces que le provocarían sorpresa máxima y focaliza su deliberación dentro de la gama de resultados que considera plausibles."
    },
    {
        "id": "shackle_17",
        "question": "¿Por qué Shackle sostiene que las tasas de interés no pueden guiar mecánicamente a la economía hacia el equilibrio general?",
        "options": [
            "Porque las tasas de interés están prohibidas en los países islámicos.",
            "Porque la rentabilidad esperada de los proyectos de inversión depende primordialmente de visiones imaginadas y estados de confianza psicológica que fluctúan de forma impredecible.",
            "Porque los bancos comerciales modifican sus tasas de interés cada cinco minutos.",
            "Porque los contratos de crédito se pactan exclusivamente en moneda extranjera."
        ],
        "correct_index": 1,
        "explanation": "La tasa de interés es solo el costo de oportunidad monetario; lo decisivo es la imagen mental que el empresario tiene del futuro. Si el empresario prevé un desastre, ninguna rebaja en la tasa de interés lo inducirá a invertir."
    },
    {
        "id": "shackle_18",
        "question": "¿Qué postura asume Shackle respecto a la tecnocracia de los bancos centrales que pretenden 'calibrar' la economía?",
        "options": [
            "Un profundo escepticismo, señalando que la autoridad no puede anticipar cómo reaccionará la imaginación de millones de agentes ante medidas de política económica.",
            "Una defensa entusiasta de los algoritmos de inteligencia artificial para fijar la masa monetaria.",
            "La recomendación de que los banqueros centrales sean elegidos de por vida por el Papa.",
            "La propuesta de sustituir a los economistas por ingenieros nucleares."
        ],
        "correct_index": 0,
        "explanation": "Shackle advierte contra la soberbia tecnocrática: cada anuncio del Banco Central es interpretado de manera subjetiva y creativa por los agentes, pudiendo provocar reacciones totalmente opuestas a las previstas en los modelos."
    },
    {
        "id": "shackle_19",
        "question": "¿Cuál es el título del influyente libro publicado por George L. S. Shackle en 1972 donde sintetiza su pensamiento epistemológico?",
        "options": [
            "The General Theory of Employment, Interest and Money.",
            "Epistemics and Economics: A Critique of Economic Doctrines.",
            "A Monetary History of the United States.",
            "Capital and Interest in Economic Development."
        ],
        "correct_index": 1,
        "explanation": "En 'Epistemics and Economics' (1972), Shackle formula su ataque sistemático a la economía ortodoxa, argumentando que una disciplina que ignore la naturaleza del conocimiento humano y el tiempo no puede considerarse ciencia."
    },
    {
        "id": "shackle_20",
        "question": "¿Por qué el marco de Shackle es fundamental para comprender las crisis financieras contemporáneas?",
        "options": [
            "Porque enseña a los bancos a calcular el valor en riesgo (VaR) con un 99% de precisión.",
            "Porque explica cómo la complacencia generada por convenciones frágiles puede desmoronarse repentinamente ante un 'cisne negro' de alta sorpresa, desatando una parálisis de crédito y huida a la liquidez.",
            "Porque demuestra que las crisis financieras son causadas exclusivamente por el gasto público.",
            "Porque propone eliminar el dinero fiduciario y regresar al trueque."
        ],
        "correct_index": 1,
        "explanation": "La teoría de Shackle explica la anatomía de los colapsos imprevistos (eventos tipo cisne negro de Taleb): cuando la realidad perfora las convenciones imaginadas, la sorpresa desata la parálisis absoluta del sistema financiero."
    }
]

# -------------------------------------------------------------
# 11. HERNANDO ZULETA G. (& PHILIP CAGAN) (20 preguntas)
# -------------------------------------------------------------
bank_part2["zuleta_cagan"] = [
    {
        "id": "zuleta_1",
        "question": "¿Cuál es la variable monetaria fundamental que actúa como la 'base imponible' del impuesto inflacionario en el modelo de Hernando Zuleta (1995)?",
        "options": [
            "El agregado amplio M3 incluyendo títulos de deuda pública.",
            "La Base Monetaria (B = Efectivo en manos del público + Reservas bancarias legales inmovilizadas en el Banco Central).",
            "El volumen total de créditos comerciales a mediano plazo.",
            "El saldo de las cuentas corrientes bancarias en moneda extranjera."
        ],
        "correct_index": 1,
        "explanation": "La base imponible sobre la cual el Estado ejerce su monopolio legal de emisión coercitiva para extraer recursos reales de la sociedad es la Base Monetaria fiduciaria no remunerada."
    },
    {
        "id": "zuleta_2",
        "question": "¿Cómo se formaliza la función de demanda de saldos monetarios reales de Philip Cagan (1956) para economías de alta inflación utilizada por Zuleta?",
        "options": [
            "m = A · e^(-α · π^e), donde m = M/P, π^e es la inflación esperada y α es la semielasticidad de la demanda de dinero.",
            "m = k · P · Y, donde k es una constante institucional fija.",
            "m = √(2bY / r), derivada de los costos de corretaje bancario.",
            "m = Yp · (1 - w), basada en la riqueza humana de largo plazo."
        ],
        "correct_index": 0,
        "explanation": "Función canónica de Cagan para hiperinflaciones: m = A · e^(-α · π^e). A medida que la inflación esperada sube, la demanda de saldos reales se derrumba de forma exponencial."
    },
    {
        "id": "zuleta_3",
        "question": "¿Qué mide el parámetro 'α' en la función de demanda de dinero de Philip Cagan m = A · e^(-α · π)?",
        "options": [
            "La propensión marginal a consumir de los asalariados.",
            "La semielasticidad de la demanda de saldos reales respecto a la tasa de inflación: α = - (1/m) · (dm/dπ).",
            "La tasa natural de crecimiento del producto bruto interno.",
            "El coeficiente de encaje bancario legal fijado por el Banco Central."
        ],
        "correct_index": 1,
        "explanation": "Alfa mide el porcentaje en que cae la demanda de saldos reales por cada punto porcentual que aumenta la tasa esperada de inflación (la sensibilidad de la huida del dinero)."
    },
    {
        "id": "zuleta_4",
        "question": "¿Cuál es la definición analítica exacta del 'Impuesto Inflacionario' (TI) en términos reales de flujo?",
        "options": [
            "TI = Gasto público - Recaudación tributaria ordinaria.",
            "TI = π · m = (P_dot / P) · (M / P), la tasa de depreciación monetaria multiplicada por el stock de saldos monetarios reales.",
            "TI = M_dot / P, la cantidad física de nuevos billetes impresos por mes.",
            "TI = r · B, el rendimiento devengado por las reservas bancarias."
        ],
        "correct_index": 1,
        "explanation": "El Impuesto Inflacionario es la pérdida de capital real que sufren los tenedores de saldos monetarios debido a la erosión de su poder adquisitivo: TI = π · m."
    },
    {
        "id": "zuleta_5",
        "question": "¿Cuál es la definición analítica del 'Señoreaje' (SE) percibido por el gobierno?",
        "options": [
            "Los impuestos arancelarios cobrados en las aduanas portuarias.",
            "SE = M_dot / P = (dM/dt) / P, el poder de compra real de los nuevos recursos brutos emitidos por la autoridad monetaria.",
            "SE = π · (Y - C), la tasa de ahorro forzoso de las familias.",
            "SE = B / (1 + r), el valor presente de los bonos del tesoro."
        ],
        "correct_index": 1,
        "explanation": "El Señoreaje mide el poder adquisitivo de los nuevos billetes puestos en circulación: representa los bienes y servicios reales que el Estado adquiere directamente mediante emisión monetaria."
    },
    {
        "id": "zuleta_6",
        "question": "¿Cuál es la ecuación dinámica que vincula al Señoreaje (SE) con el Impuesto Inflacionario (TI) y la variación de saldos reales en el tiempo?",
        "options": [
            "SE = TI · m_dot",
            "SE = m_dot + TI, derivada de la regla de la derivada del cociente de saldos reales m = M/P.",
            "SE = TI - π^2 / 2",
            "SE = m_dot / TI"
        ],
        "correct_index": 1,
        "explanation": "Derivando m = M/P respecto al tiempo: m_dot = (M_dot/P) - (P_dot/P)·m = SE - TI. Reordenando términos: SE = m_dot + TI. El señoreaje es igual al cambio en los saldos reales más el impuesto inflacionario."
    },
    {
        "id": "zuleta_7",
        "question": "¿Qué ocurre con la relación entre Señoreaje e Impuesto Inflacionario en una economía que se encuentra en 'Estado Estacionario' (m_dot = 0)?",
        "options": [
            "El señoreaje se reduce a cero a perpetuidad.",
            "El Señoreaje coincide exactamente con el Impuesto Inflacionario: SE = TI = π · m.",
            "El impuesto inflacionario duplica al señoreaje bruto.",
            "El gobierno debe declarar la quiebra soberana de sus pasivos."
        ],
        "correct_index": 1,
        "explanation": "En estado estacionario la tenencia de saldos reales es constante (m_dot = 0). Por ende, SE = 0 + TI = π · m. Todo el señoreaje recaudado coincide con la recaudación del impuesto inflacionario."
    },
    {
        "id": "zuleta_8",
        "question": "¿En qué consiste la 'Curva de Laffer del Señoreaje' analizada matemáticamente por Hernando Zuleta?",
        "options": [
            "En la relación inversa entre el gasto militar y la inversión pública.",
            "En la existencia de rendimientos decrecientes y un máximo en la recaudación real del impuesto inflacionario debido a la huida de los saldos reales ante tasas crecientes de emisión.",
            "En la teoría de que emitir billetes reduce el desempleo a cero.",
            "En el vínculo lineal directo e infinito entre inflación y recaudación fiscal."
        ],
        "correct_index": 1,
        "explanation": "Al igual que con cualquier impuesto, al subir la alícuota (π), la base imponible (m) se achica. Al principio la recaudación sube, pero llega un punto donde la caída de la base supera a la suba de la tasa, cayendo la recaudación real."
    },
    {
        "id": "zuleta_9",
        "question": "¿Cómo se deriva matemáticamente la tasa de inflación que maximiza la recaudación del impuesto inflacionario (π*) a partir de la demanda de Cagan TI = π · A · e^(-α · π)?",
        "options": [
            "dTI/dπ = A · e^(-απ) · (1 - α · π) = 0  ===>  π* = 1 / α",
            "dTI/dπ = 1 + α / π = 0  ===>  π* = α",
            "dTI/dπ = A · π · e^(-α) = 0  ===>  π* = e",
            "dTI/dπ = α · ln(π) = 0  ===>  π* = 0"
        ],
        "correct_index": 0,
        "explanation": "Derivada del producto: dTI/dπ = A·e^(-απ) + π·A·(-α)·e^(-απ) = A·e^(-απ)·(1 - α·π). Igualando a cero: 1 - α·π = 0, por lo que π* = 1/α. La tasa que maximiza la recaudación es la inversa de la semielasticidad."
    },
    {
        "id": "zuleta_10",
        "question": "¿Cuál es la recaudación MÁXIMA de señoreaje en estado estacionario (SE_max) que el gobierno puede obtener según el modelo de Cagan y Zuleta?",
        "options": [
            "SE_max = A · α",
            "SE_max = (1 / α) · A · e^(-1) = A / (α · e)",
            "SE_max = infinito, siempre que el Banco Central no se detenga.",
            "SE_max = A · e^α"
        ],
        "correct_index": 1,
        "explanation": "Reemplazando π* = 1/α en la función: TI(1/α) = (1/α) · A · e^(-α · (1/α)) = (1/α) · A · e^(-1) = A / (α · e). Este es el límite físico y matemático de recursos reales que el Estado puede extraer de la sociedad."
    },
    {
        "id": "zuleta_11",
        "question": "¿Qué ocurre si el gobierno enfrenta un déficit fiscal real estructural MAYOR que el máximo de la curva de Laffer (D > A / (α · e)) y lo financia con emisión monetaria?",
        "options": [
            "La economía alcanza un equilibrio de precios estables y pleno empleo.",
            "Se desata una dinámica hiperinflacionaria explosiva: como la recaudación no alcanza a cubrir el bache, el gobierno emite más rápido, destruyendo la demanda de dinero hasta colapsar el sistema monetario.",
            "El tipo de cambio nominal se aprecia automáticamente frente a las divisas extranjeras.",
            "Los bancos comerciales aumentan sus reservas de oro físico en el exterior."
        ],
        "correct_index": 1,
        "explanation": "Génesis matemática de las hiperinflaciones: si el déficit supera el máximo de Laffer, no existe tasa de inflación estacionaria que financie el gasto. Acelerar la emisión reduce la recaudación real, desatando la espiral hiperinflacionaria."
    },
    {
        "id": "zuleta_12",
        "question": "¿En qué consiste el tramo ineficiente o 'lado equivocado' de la Curva de Laffer del señoreaje (π > 1/α)?",
        "options": [
            "Un tramo donde la inflación es negativa pero la deuda pública sube.",
            "Una zona donde tasas de inflación más altas rinden MENOR recaudación fiscal real que antes, debido a la huida masiva del público hacia el dólar o bienes físicos.",
            "Un área donde los salarios reales crecen por encima de la productividad del trabajo.",
            "La región donde el coeficiente de encaje bancario se vuelve negativo."
        ],
        "correct_index": 1,
        "explanation": "Operar a la derecha de π* = 1/α es irracional y destructivo: la economía padece una inflación brutal pero el gobierno recauda menos recursos reales que si tuviera una inflación más baja."
    },
    {
        "id": "zuleta_13",
        "question": "¿Cómo utiliza el gobierno la manipulación de los encajes bancarios obligatorios según el análisis de Zuleta?",
        "options": [
            "Para incentivar a las pymes a tomar préstamos productivos.",
            "Para ampliar artificialmente la base imponible cautiva del impuesto inflacionario, obligando a los bancos a congelar más fondos a tasa cero en el Banco Central.",
            "Para permitir la apertura de nuevas sucursales bancarias en zonas rurales.",
            "Para pagar los sueldos de los directores de las escuelas públicas."
        ],
        "correct_index": 1,
        "explanation": "Al elevar el coeficiente de encaje (r), el gobierno fuerza a los bancos a inmovilizar reservas no remuneradas en el Banco Central, ensanchando la base monetaria cautiva para exprimir más señoreaje a corto plazo."
    },
    {
        "id": "zuleta_14",
        "question": "¿Qué postula la teoría de la 'Dominancia Fiscal' (Fiscal Dominance) presente en el ensayo de Zuleta?",
        "options": [
            "Que la política monetaria domina y ordena los presupuestos de todos los ministerios.",
            "Que la política monetaria está completamente subordinada y maniatada por las necesidades de financiamiento del déficit presupuestario del Tesoro público.",
            "Que el poder judicial puede destituir al ministro de hacienda por decreto.",
            "Que el gasto fiscal se financia exclusivamente con donaciones del sector privado."
        ],
        "correct_index": 1,
        "explanation": "Bajo dominancia fiscal, el Banco Central carece de autonomía real: su función queda reducida a emitir los billetes necesarios para cubrir el bache de caja del Estado que no puede financiarse con deuda ni impuestos."
    },
    {
        "id": "zuleta_15",
        "question": "¿Por qué el proceso de 'Dolarización espontánea' o sustitución de monedas reduce drásticamente los ingresos por señoreaje del gobierno?",
        "options": [
            "Porque la Reserva Federal de EE.UU. confisca las cuentas bancarias de los ciudadanos.",
            "Porque al refugiarse el público en divisas extranjeras para pagos y ahorros, la demanda de moneda nacional colapsa (cae el parámetro A y sube α), encogiendo la base imponible del impuesto inflacionario.",
            "Porque los comercios cobran recargos aduaneros sobre las transacciones en efectivo.",
            "Porque la inflación de los Estados Unidos se traslada automáticamente a los precios locales."
        ],
        "correct_index": 1,
        "explanation": "Al huir hacia el dólar, el público desmonetiza la economía local. La base de dinero sobre la que el gobierno puede cobrar el impuesto inflacionario se evapora, haciendo colapsar la recaudación real."
    },
    {
        "id": "zuleta_16",
        "question": "En presencia de crecimiento del producto real a una tasa g (Y_dot / Y = g), ¿cómo se modifica la recaudación de señoreaje no inflacionario?",
        "options": [
            "El señoreaje se extingue por completo.",
            "El gobierno puede emitir dinero sin generar inflación a una tasa igual a g, recaudando señoreaje real gracias al aumento natural de la demanda de saldos de transacción.",
            "La inflación se acelera de forma directamente proporcional a g.",
            "El coeficiente de encaje bancario debe multiplicarse por g."
        ],
        "correct_index": 1,
        "explanation": "Si la economía crece, el público demanda más dinero genuino para transacciones. El Banco Central puede emitir a esa misma tasa sin causar inflación, recaudando un 'señoreaje no inflacionario' legítimo."
    },
    {
        "id": "zuleta_17",
        "question": "¿Cuál es la prescripción institucional indispensable para erradicar definitivamente la inflación originada en señoreaje fiscal?",
        "options": [
            "Aumentar el número de billetes impresos por cada habitante.",
            "Eliminar el déficit fiscal estructural y consagrar por ley la prohibición absoluta de que el Banco Central financie al Tesoro público (independencia orgánica).",
            "Fijar precios máximos en los comercios de alimentos y bebidas.",
            "Aumentar los impuestos a las exportaciones industriales."
        ],
        "correct_index": 1,
        "explanation": "La solución de raíz exige equilibrio presupuestario y cortar el cordón umbilical entre el Banco Central y la Tesorería, prohibiendo la monetización espuria de los desequilibrios fiscales."
    },
    {
        "id": "zuleta_18",
        "question": "¿Cómo se vincula el modelo de Zuleta y Cagan con el Efecto Olivera-Tanzi?",
        "options": [
            "Demuestran que el efecto Olivera-Tanzi no existe en América Latina.",
            "El efecto Olivera-Tanzi refuerza la dinámica de Cagan: al destruir la inflación los ingresos tributarios reales ordinarios, empuja al gobierno a depender aún más del señoreaje, acelerando la emisión.",
            "Ambos modelos postulan que la recaudación impositiva crece con la inflación de forma infinita.",
            "Olivera y Tanzi demostraron que el parámetro alfa es siempre igual a cero."
        ],
        "correct_index": 1,
        "explanation": "Complementariedad directa: la erosión de los impuestos ordinarios por rezagos de cobranza (Olivera-Tanzi) agranda el déficit fiscal efectivo, forzando a emitir más señoreaje y acelerando la trayectoria hacia la hiperinflación."
    },
    {
        "id": "zuleta_19",
        "question": "¿Qué ocurre con el costo social y el bienestar de los agentes económicos bajo un régimen de alto impuesto inflacionario?",
        "options": [
            "Aumenta el bienestar de los asalariados gracias a la mayor cantidad de billetes en circulación.",
            "Se produce una pérdida masiva de peso muerto (deadweight loss): distorsión del sistema de precios, costos de suela de zapatos (frecuentes viajes al banco) y castigo regresivo a los sectores más vulnerables no bancarizados.",
            "Las familias aumentan su consumo de bienes de capital duraderos importados.",
            "El coeficiente de Gini mejora sustancialmente en toda la sociedad."
        ],
        "correct_index": 1,
        "explanation": "El impuesto inflacionario es el tributo más regresivo e ineficiente: castiga con máxima dureza a los hogares de menores ingresos que no tienen acceso a instrumentos financieros indexados ni divisas para protegerse."
    },
    {
        "id": "zuleta_20",
        "question": "¿Por qué el artículo de Zuleta (Borradores de Economía, Banco de la República de Colombia, 1995) es considerado una pieza pedagógica clásica?",
        "options": [
            "Porque explica la historia colonial de la Nueva Granada en el siglo XVIII.",
            "Porque formaliza con claridad matemática rigurosa los límites exactos de la emisión monetaria, desmitificando la ilusión de que el gasto público puede financiarse indefinidamente imprimiendo billetes.",
            "Porque propone eliminar el dinero fiduciario en Colombia y sustituirlo por café.",
            "Porque defiende la fijación de tasas de interés activas subsidiadas por decreto."
        ],
        "correct_index": 1,
        "explanation": "Zuleta sintetiza con elegancia matemática la restricción presupuestaria intertemporal del Estado y demuestra analíticamente que imprimir dinero choca contra el muro inexorable de la curva de Laffer del señoreaje."
    }
]

# -------------------------------------------------------------
# 12. HARRY G. JOHNSON (20 preguntas)
# -------------------------------------------------------------
bank_part2["harry_johnson"] = [
    {
        "id": "johnson_1",
        "question": "¿Cuál es el objetivo principal del influyente ensayo de Harry G. Johnson 'Revolución y contrarrevolución en economía' (1971)?",
        "options": [
            "Proponer un nuevo impuesto a las transacciones de divisas en Londres.",
            "Analizar desde una perspectiva sociológica e histórica cómo nacen, triunfan, se institucionalizan y decaen las corrientes teóricas en la profesión económica (en particular el keynesianismo y el monetarismo).",
            "Demostrar que los modelos matemáticos deben ser prohibidos en las universidades.",
            "Defender el retorno incondicional de los Estados Unidos al patrón oro puro."
        ],
        "correct_index": 1,
        "explanation": "Johnson examina la sociología de la profesión académica: analiza las condiciones sociales, políticas y metodológicas que permitieron la victoria de la Revolución Keynesiana en los años 30 y la Contrarrevolución Monetarista en los 60."
    },
    {
        "id": "johnson_2",
        "question": "¿Cuál es la primera condición fundamental identificada por Johnson para que una teoría económica logre una revolución exitosa?",
        "options": [
            "Obtener el financiamiento de grandes bancos comerciales privados.",
            "Atacar a una ortodoxia intelectual establecida que ha fracasado visiblemente ante una crisis empírica real de gran magnitud y relevancia social.",
            "Traducir todos sus textos al idioma francés y alemán.",
            "Publicar artículos exclusivamente en periódicos de tirada masiva."
        ],
        "correct_index": 1,
        "explanation": "Ninguna teoría triunfa en el vacío. Debe haber un fracaso empírico inocultable de la ortodoxia previa: el desempleo masivo de la Gran Depresión destruyó a los clásicos; la inflación de posguerra desgastó al keynesianismo."
    },
    {
        "id": "johnson_3",
        "question": "¿Por qué triunfó con tanta rapidez la Revolución Keynesiana en los años treinta según Harry Johnson?",
        "options": [
            "Porque la ortodoxia clásica pregonaba que el mercado resolvía todo mientras millones de personas estaban desocupadas en la Gran Depresión, ofreciendo Keynes una explicación y una salida activa con la política fiscal.",
            "Porque Keynes era miembro de la Cámara de los Lores británica.",
            "Porque los bancos comerciales estadounidenses subsidiaron la difusión de la Teoría General.",
            "Porque la teoría clásica carecía de ecuaciones matemáticas."
        ],
        "correct_index": 0,
        "explanation": "Los economistas clásicos no tenían respuesta ante el desempleo masivo del 25%. Keynes proveyó una teoría sólida que explicaba el desequilibrio y otorgaba a los gobiernos un rol constructivo mediante el gasto público."
    },
    {
        "id": "johnson_4",
        "question": "¿Cuál es el segundo requisito sociológico para el éxito académico de una nueva corriente según Johnson?",
        "options": [
            "Tener una metodología nueva, sofisticada y difícil que entusiasme a investigadores jóvenes y margine a los profesores de mayor edad que no la dominan.",
            "Exigir que todos los profesores universitarios tengan menos de treinta años.",
            "Prohibir el dictado de cátedras de historia del pensamiento económico.",
            "Utilizar únicamente gráficos dibujados a mano alzada."
        ],
        "correct_index": 0,
        "explanation": "El factor generacional: una nueva teoría debe ofrecer un instrumental técnico desafiante que permita a los jóvenes investigadores publicar con ventaja frente a los profesores consagrados incapaces de reciclarse."
    },
    {
        "id": "johnson_5",
        "question": "¿En qué consistió la genial 'Maniobra Táctica' de Milton Friedman para lanzar la contrarrevolución monetarista desentrañada por Johnson?",
        "options": [
            "En resucitar la rígida teoría cuantitativa clásica con velocidad constante V.",
            "En no resucitar la vieja teoría clásica (fácilmente refutable), sino reformular la teoría cuantitativa como una función de DEMANDA DE DINERO ESTABLE adoptando el propio lenguaje de liquidez de Keynes.",
            "En solicitar que la Reserva Federal sea clausurada por la policía.",
            "En convencer a los sindicatos de renunciar al salario mínimo legal."
        ],
        "correct_index": 1,
        "explanation": "Friedman fue brillante tácticamente: adoptó la teoría de carteras y preferencia por la liquidez keynesiana, pero invirtió sus conclusiones demostrando que la demanda de dinero era sumamente estable y la política fiscal ineficaz."
    },
    {
        "id": "johnson_6",
        "question": "¿Cuál fue la gran vulnerabilidad empírica del keynesianismo de posguerra que permitió el avance arrollador del monetarismo de Chicago?",
        "options": [
            "La falta de computadoras en las oficinas gubernamentales de Londres.",
            "La incapacidad teórica y práctica de la síntesis keynesiana para explicar y frenar la aceleración inflacionaria en economías con pleno empleo.",
            "El aumento de las exportaciones de automóviles alemanes y japoneses.",
            "La negativa de los sindicatos a negociar convenios colectivos de trabajo."
        ],
        "correct_index": 1,
        "explanation": "Diseñado para combatir el desempleo deflacionario, el keynesianismo fiscalista no supo responder a la estanflación y a la inflación continua de los años 60 y 70, abriendo la puerta a la contrarrevolución de Friedman."
    },
    {
        "id": "johnson_7",
        "question": "¿Qué atractivo político e ideológico ofreció el monetarismo a los gobiernos conservadores según Harry Johnson?",
        "options": [
            "Un programa de estatización generalizada de las empresas de telecomunicaciones.",
            "Una justificación científica rigurosa para limitar el gasto público, desmantelar regulaciones e intervenciones estatales y atar al Banco Central a reglas rígidas de mercado.",
            "Una doctrina para subsidiar el transporte ferroviario de pasajeros.",
            "Una propuesta para financiar las guerras coloniales con emisión de deuda fiduciaria."
        ],
        "correct_index": 1,
        "explanation": "El monetarismo suministró a la política conservadora (Nixon, Thatcher, Reagan) un argumento académico irrebatible: la inflación la crea el Estado con el gasto público y la emisión; la solución es reducir el Estado y dejar operar al mercado."
    },
    {
        "id": "johnson_8",
        "question": "¿Cuál es el tercer requisito identificado por Johnson respecto al 'producto intelectual' que ofrece una nueva teoría?",
        "options": [
            "Debe incluir anécdotas cómicas para entretener a los legisladores del parlamento.",
            "Debe poseer una apariencia de realismo e intuición atractiva combinada con un programa fértil de contrastación empírica y recetas aplicables para los gobiernos.",
            "Debe proponer la creación de cinco nuevos ministerios en el poder ejecutivo.",
            "Debe garantizar que el comercio internacional se realice sin uso de barcos."
        ],
        "correct_index": 1,
        "explanation": "La teoría debe ser intuitiva para la opinión pública (como 'la inflación la causa la maquinita de billetes' o 'el desempleo se arregla con obras públicas') y proveer un campo fértil de estimaciones estadísticas para tesis de posgrado."
    },
    {
        "id": "johnson_9",
        "question": "¿Por qué pronosticó proféticamente Harry Johnson en 1971 que el monetarismo entraría en decadencia con el paso del tiempo?",
        "options": [
            "Porque los billetes de papel serían reemplazados por el trueque de mercancías.",
            "Porque al convertirse en dogma gubernamental, la innovación financiera y los cambios en los mercados volverían inestables a los agregados monetarios, minando su capacidad predictiva.",
            "Porque la Escuela de Chicago cerraría su departamento de economía.",
            "Porque la inflación desaparecería para siempre de las economías desarrolladas."
        ],
        "correct_index": 1,
        "explanation": "Profecía cumplida de Johnson: en los años 80 la innovación financiera (cajeros, fondos mutuos, tarjetas) volvió inestable la velocidad V y quebró la relación entre M1/M2 y el PBI, forzando a los bancos centrales a abandonar las metas de agregados."
    },
    {
        "id": "johnson_10",
        "question": "¿Qué distinción establece Harry Johnson entre el monetarismo como investigación científica de Chicago y el monetarismo vulgar de la política?",
        "options": [
            "El monetarismo científico se enseñaba en latín y el vulgar en inglés.",
            "El científico reconocía rezagos largos, problemas metodológicos y complejidades empíricas; el vulgar se redujo a eslóganes simplistas que prometían resolver la economía recortando mecánicamente el crédito.",
            "El científico defendía a los sindicatos y el vulgar a las corporaciones financieras.",
            "No existía ninguna diferencia conceptual entre ambos enfoques."
        ],
        "correct_index": 1,
        "explanation": "Johnson advierte cómo una investigación econométrica cautelosa y sofisticada (Friedman y Schwartz) fue degradada por los círculos mediáticos y políticos en una fórmula mágica de austeridad extrema e indiferencia al costo social."
    },
    {
        "id": "johnson_11",
        "question": "En el debate sobre el dinero, ¿cómo describe Johnson la pugna entre M1 y M2?",
        "options": [
            "Como una disputa irrelevante entre estadísticos del censo nacional.",
            "Como el campo de batalla donde el monetarismo buscó probar que 'el dinero importa' demostrando que un agregado gobernable por la Fed mantenía una relación estable con la actividad real.",
            "Como un conflicto diplomático entre el Tesoro de EE.UU. y el Banco de Francia.",
            "Como una discusión sobre el tamaño físico de los billetes de curso legal."
        ],
        "correct_index": 1,
        "explanation": "La elección de M2 fue la pieza clave de la ofensiva de Chicago para derrotar la tesis keynesiana de que la política monetaria era secundaria frente a la política fiscal."
    },
    {
        "id": "johnson_12",
        "question": "¿Cuál es la postura de Johnson respecto al papel de las 'grandes personalidades' carismáticas en las revoluciones económicas?",
        "options": [
            "Afirma que los individuos no importan y que la historia económica es totalmente impersonal.",
            "Reconoce el rol decisivo de líderes intelectuales brillantes y polemistas extraordinarios como Keynes en los años 30 y Friedman en los 60 para cohesionar escuelas de discípulos.",
            "Sostiene que los líderes de las revoluciones económicas deben ser banqueros en ejercicio.",
            "Argumenta que las teorías económicas son redactadas por comités anónimos del senado."
        ],
        "correct_index": 1,
        "explanation": "Tanto Keynes como Friedman combinaban rigor analítico con una prodigiosa capacidad de debate público, persuasión retórica y liderazgo de discípulos devotos que impulsaron sus respectivas revoluciones."
    },
    {
        "id": "johnson_13",
        "question": "¿Cómo evaluaba Harry Johnson el estado de la macroeconomía de la síntesis keynesiana a finales de la década de 1960?",
        "options": [
            "Como una disciplina en la cúspide de su perfección matemática y empírica.",
            "Como una ortodoxia envejecida, complaciente y burocratizada que había olvidado las preguntas fundamentales y se limitaba a ajustar parámetros en modelos econométricos gigantistas.",
            "Como una corriente clandestina perseguida por los gobiernos occidentales.",
            "Como una escuela que carecía de inserción en las universidades de élite."
        ],
        "correct_index": 1,
        "explanation": "El keynesianismo se había vuelto dogmático y acomodaticio, despreciando el análisis del dinero y confiando ciegamente en ecuaciones fiscales que ya no encajaban con la realidad inflacionaria emergente."
    },
    {
        "id": "johnson_14",
        "question": "¿Qué papel cumplieron las controversias sobre la 'Curva de Phillips' en el ascenso del monetarismo según Johnson?",
        "options": [
            "La curva de Phillips demostró que la inflación era imposible de predecir.",
            "La demostración de Friedman de que no existía un trade-off explotable a largo plazo fue el golpe de gracia teórico que demolió el activismo de política keynesiano.",
            "La curva de Phillips forzó el cierre de las bolsas de valores europeas.",
            "Los economistas de Chicago demostraron que el desempleo y la inflación tenían signo negativo idéntico."
        ],
        "correct_index": 1,
        "explanation": "Al probar que la curva de Phillips se verticalizaba en el largo plazo por la corrección de expectativas, Friedman quitó al keynesianismo su principal herramienta de justificación del gasto discrecional."
    },
    {
        "id": "johnson_15",
        "question": "¿Qué advierte Johnson sobre el peligro de que una contrarrevolución económica triunfante descarte los aciertos de la teoría que desplazó?",
        "options": [
            "Que se corre el riesgo de quemar los libros de la biblioteca del Congreso.",
            "Que al arrojar por la borda todo el instrumental keynesiano, el monetarismo se volvía ciego ante problemas legítimos de desempleo involuntario, fallas de coordinación y rigideces de corto plazo.",
            "Que los salarios de los profesores de economía disminuyen un 50%.",
            "Que los gobiernos dejan de calcular el producto bruto interno."
        ],
        "correct_index": 1,
        "explanation": "En su afán de victoria doctrinal, las contrarrevoluciones caen en el reduccionismo: el monetarismo tendió a ignorar que las recesiones provocan sufrimiento social real y que el dinero no siempre es neutral en la práctica cotidiana."
    },
    {
        "id": "johnson_16",
        "question": "¿En qué prestigiosas universidades se desempeñó Harry G. Johnson como profesor influyente durante las controversias monetarias?",
        "options": [
            "En la Universidad de Moscú y la Universidad de Pekín.",
            "Simultáneamente en la Universidad de Chicago y en la London School of Economics (LSE).",
            "En la Universidad de Salamanca y la Sorbona de París.",
            "Exclusivamente en el Banco Mundial en Washington."
        ],
        "correct_index": 1,
        "explanation": "Johnson fue una figura transatlántica legendaria: cruzaba el océano constantemente enseñando en Chicago (epicentro del monetarismo) y en la LSE (epicentro de la macroeconomía británica), siendo testigo privilegiado de los debates."
    },
    {
        "id": "johnson_17",
        "question": "¿Qué recomendación metodológica deja el ensayo de Johnson a los estudiantes e investigadores de la ciencia económica?",
        "options": [
            "Aceptar ciegamente el manual de texto oficial que enseñe el profesor de turno.",
            "Mantener un escepticismo crítico y saludable frente a las modas académicas, entendiendo que las teorías económicas responden a coyunturas históricas específicas y a intereses profesionales y políticos.",
            "Abandonar el estudio de la economía y dedicarse a la literatura de ficción.",
            "Memorizar de memoria las ecuaciones algebraicas sin comprender su significado social."
        ],
        "correct_index": 1,
        "explanation": "Lección suprema para examen: ninguna teoría económica es una verdad absoluta o intemporal. Todas son construcciones humanas condicionadas por crisis históricas, disputas de poder universitario y conveniencias políticas."
    },
    {
        "id": "johnson_18",
        "question": "¿Cómo analiza Johnson el impacto de la contrarrevolución monetarista en la política de los Bancos Centrales de los países anglosajones?",
        "options": [
            "Los bancos centrales dejaron de intervenir en los mercados de divisas.",
            "Obligó a los banqueros centrales a abandonar la fijación exclusiva de tasas de interés de corto plazo y a adoptar metas cuantitativas de agregados monetarios durante los años setenta.",
            "Provocó la eliminación de los billetes de curso legal en Gran Bretaña.",
            "Determinó que los gobernadores bancarios fueran nombrados por los líderes sindicales."
        ],
        "correct_index": 1,
        "explanation": "Bajo la influencia de Friedman, tanto la Fed como el Banco de Inglaterra adoptaron regímenes de control estricto de agregados monetarios (targeting monetario), cambiando para siempre la praxis de la banca central."
    },
    {
        "id": "johnson_19",
        "question": "¿Por qué el artículo de Harry Johnson sigue siendo de lectura obligatoria en los programas universitarios de Teoría Monetaria?",
        "options": [
            "Porque contiene la fórmula matemática de la velocidad del dinero.",
            "Porque proporciona una autopsia lúcida y desapasionada de las disputas doctrinarias que forjaron la macroeconomía moderna, desnudando la lógica con la que las escuelas compiten por la hegemonía.",
            "Porque fue premiado con el Premio Nobel de Economía en 1971.",
            "Porque enseña a los estudiantes a redactar balances contables comerciales."
        ],
        "correct_index": 1,
        "explanation": "Es una obra maestra de epistemología y sociología de la economía que enseña a pensar críticamente la disciplina, permitiendo entender por qué Keynes desplazó a los clásicos y por qué Chicago desplazó a Keynes."
    },
    {
        "id": "johnson_20",
        "question": "¿Cuál es la conclusión final de Johnson sobre el ciclo de vida de las corrientes en el pensamiento económico?",
        "options": [
            "Que una teoría dominante jamás pierde su condición de verdad incuestionable.",
            "Que cada revolución engendra con el tiempo su propia contrarrevolución a medida que sus promesas chocan contra nuevas realidades que no puede explicar, dando paso a una síntesis o a un nuevo paradigma.",
            "Que la economía dejó de evolucionar tras la publicación de la Teoría General de Keynes.",
            "Que las teorías económicas solo cambian cuando cambia la moneda de curso legal del país."
        ],
        "correct_index": 1,
        "explanation": "El proceso del pensamiento económico es dialéctico: tesis, antítesis y síntesis. Ningún paradigma es inmune al paso del tiempo; el éxito engendra dogmatismo, y el dogmatismo engendra la próxima revolución."
    }
]

# -------------------------------------------------------------
# 13. CLÁSICOS Y POSKEYNESIANOS (FISHER, PIGOU, BAUMOL, TOBIN) (20 preguntas)
# -------------------------------------------------------------
bank_part2["clasicos_poskeynesianos"] = [
    {
        "id": "clasicos_1",
        "question": "¿Cómo se formaliza la clásica 'Ecuación de Intercambio' de Irving Fisher (The Purchasing Power of Money, 1911)?",
        "options": [
            "M · V = P · T, donde M es la cantidad de dinero, V la velocidad de circulación, P el nivel de precios y T el volumen físico de transacciones.",
            "M = k · P · Y, derivada del ahorro en saldos de caja.",
            "M = √(2bY / r), basada en la optimización de inventarios.",
            "M / P = L1(Y) + L2(r), basada en la preferencia por la liquidez."
        ],
        "correct_index": 0,
        "explanation": "La ecuación de intercambio de Fisher M · V = P · T es una identidad contable que se transforma en teoría causal clásica al postular que V y T son constantes en el corto plazo determinadas por factores reales e institucionales."
    },
    {
        "id": "clasicos_2",
        "question": "¿Qué supuestos fundamentales transforman la ecuación de intercambio de Fisher en la Teoría Cuantitativa clásica estricta?",
        "options": [
            "Que los salarios nominales están fijados por los sindicatos y los precios son rígidos a la baja.",
            "Que la velocidad V está fija por hábitos y tecnologías de pago, y el volumen de transacciones T está fijo en el pleno empleo de factores; por ende, M determina proporcionalmente a P.",
            "Que el dinero devenga una tasa de interés real fijada por el Banco Central.",
            "Que no existen bancos comerciales ni depósitos en cuenta corriente."
        ],
        "correct_index": 1,
        "explanation": "Bajo pleno empleo (T fijo) y costumbres de pago estables (V constante), cualquier cambio porcentual en la masa monetaria M se traslada exacta y proporcionalmente al nivel general de precios P."
    },
    {
        "id": "clasicos_3",
        "question": "¿Cómo se formaliza la 'Ecuación de Cambridge' de la demanda de dinero (Marshall y Pigou, 1917/1923)?",
        "options": [
            "M^d = k · P · Y, donde k es la fracción del ingreso nominal que los agentes desean retener voluntariamente en saldos de caja.",
            "M · V = P · T, con transacciones brutas totales.",
            "M^d = f(Yp, w, rm, rb, re, πe)",
            "M^d = L1(Y) + L2(r)"
        ],
        "correct_index": 0,
        "explanation": "Marshall y Pigou introducen el enfoque de saldos de caja: M^d = k · P · Y. Ponen el acento en la decisión microeconómica individual de atesoramiento de dinero como reserva de valor y medio de cambio."
    },
    {
        "id": "clasicos_4",
        "question": "¿Cuál es la relación matemática exacta entre el parámetro 'k' de Cambridge y la velocidad de circulación 'V' de Fisher?",
        "options": [
            "k = V^2",
            "k = 1 / V, son inversos matemáticos exactos.",
            "k = V - P",
            "k = ln(V)"
        ],
        "correct_index": 1,
        "explanation": "Si M · V = P · Y, entonces M = (1/V) · P · Y. Comparando con M^d = k · P · Y, se deduce que k = 1/V. Cuanto mayor es la velocidad con que circula el dinero, menor es la proporción de saldos que se retiene en caja."
    },
    {
        "id": "clasicos_5",
        "question": "¿Qué avance analítico crucial representa el enfoque de Cambridge de Marshall y Pigou frente a la ecuación mecánica de Fisher?",
        "options": [
            "Demuestra que el dinero no tiene ninguna relación con los precios.",
            "Traslada el análisis desde una relación mecánica de pagos de intercambio hacia una decisión microeconómica de elección individual de cartera y tenencia de riqueza.",
            "Elimina el concepto de pleno empleo del análisis macroeconómico.",
            "Introduce el cálculo de probabilidades en los mercados de futuros agrícolas."
        ],
        "correct_index": 1,
        "explanation": "Cambridge convierte la teoría cuantitativa en una teoría de demanda de dinero: las personas eligen conscientemente retener una fracción k de su ingreso por conveniencia y seguridad, abriendo el camino hacia Keynes."
    },
    {
        "id": "clasicos_6",
        "question": "¿En qué consiste el célebre modelo de 'Inventarios de Demanda de Dinero' desarrollado por William Baumol (1952) y James Tobin (1956)?",
        "options": [
            "En el almacenamiento físico de lingotes de oro en cajas de seguridad subterráneas.",
            "En la optimización microeconómica de la tenencia transaccional de dinero, minimizando la suma de costos de transacción/corretaje (b) y los intereses perdidos por no tener bonos (r).",
            "En la compra masiva de inventarios de granos para especular con su precio futuro.",
            "En la teoría de que las empresas deben mantener una cantidad fija de efectivo por empleado."
        ],
        "correct_index": 1,
        "explanation": "Baumol y Tobin aplican el modelo de gestión óptima de inventarios a la liquidez: los agentes balancean el costo de convertir bonos en dinero (ir al banco, costo de corretaje b) con el costo de oportunidad de los intereses no ganados (r)."
    },
    {
        "id": "clasicos_7",
        "question": "¿Cuál es la fórmula matemática de la tenencia óptima de dinero por motivo transacción derivada por Baumol y Tobin (The Square-Root Formula)?",
        "options": [
            "M^d = √(2 · b · Y / r), donde b es el costo de corretaje, Y el ingreso real y r la tasa de interés.",
            "M^d = (b · Y) / (2 · r)",
            "M^d = 2 · b · Y · r",
            "M^d = ln(b · Y) / r"
        ],
        "correct_index": 0,
        "explanation": "Regla de la raíz cuadrada de Baumol-Tobin: el saldo monetario medio óptimo es M^d = √(2bY / r) (o √(bY / 2r) según cómo se defina el retiro promedio C/2 = √(bY / 2r))."
    },
    {
        "id": "clasicos_8",
        "question": "¿Qué elasticidades de la demanda de dinero demuestra matemáticamente el modelo de inventarios de Baumol-Tobin?",
        "options": [
            "Elasticidad-ingreso de 1.0 y elasticidad-interés de 0.0.",
            "Elasticidad-ingreso de 0.5 (existen economías de escala en el uso del dinero) y elasticidad-tasa de interés de -0.5 (el motivo transacción SÍ depende negativamente de la tasa de interés).",
            "Elasticidad-ingreso de 2.0 y elasticidad-interés de -2.0.",
            "Ambas elasticidades son infinitas debido a la trampa de liquidez."
        ],
        "correct_index": 1,
        "explanation": "Descubrimientos trascendentales de examen: 1) Elasticidad ingreso = 0.5 (al duplicar el ingreso, la demanda de dinero sube solo un 41%: economías de escala); 2) Elasticidad interés = -0.5 (refuta a Keynes al probar que la transacción también depende de r)."
    },
    {
        "id": "clasicos_9",
        "question": "¿Por qué el modelo de Baumol-Tobin corrige y perfecciona la teoría de la demanda de dinero de John Maynard Keynes?",
        "options": [
            "Porque demuestra que la demanda especulativa no existe en la economía real.",
            "Porque prueba que el motivo transacción NO depende únicamente del ingreso como creía Keynes, sino que también responde de manera negativa y elástica a la tasa de interés.",
            "Porque elimina por completo la distinción entre dinero y bonos.",
            "Porque demuestra que los bancos comerciales no pueden quebrar bajo competencia perfecta."
        ],
        "correct_index": 1,
        "explanation": "Keynes postulaba que L1 dependía solo de Y y que solo L2 dependía de r. Baumol y Tobin microfundamentan que cuando las tasas de interés son muy altas, la gente gestiona eficientemente sus saldos transaccionales, reduciendo L1."
    },
    {
        "id": "clasicos_10",
        "question": "En su ensayo seminal de 1958 ('Liquidity Preference as Behavior Towards Risk'), ¿cómo microfundamenta James Tobin la demanda especulativa de dinero?",
        "options": [
            "Mediante la teoría de juegos evolutivos en mercados oligopólicos.",
            "Mediante la teoría de selección de cartera bajo aversión al riesgo en el espacio media-varianza: los inversores diversifican entre dinero (riesgo cero, rendimiento cero) y bonos (rendimiento positivo r con riesgo de capital medido por la varianza).",
            "Asumiendo que los inversores tienen una bola de cristal con la que predicen las tasas futuras.",
            "Postulando que los agentes solo compran bonos los días lunes de cada semana."
        ],
        "correct_index": 1,
        "explanation": "Tobin supera la debilidad keynesiana (que exigía expectativas inflexibles sobre una tasa normal): demuestra que inversores con aversión al riesgo diversifican eficientemente entre dinero seguro y bonos riesgosos según su perfil de riesgo-retorno."
    },
    {
        "id": "clasicos_11",
        "question": "En el modelo de carteras de Tobin (1958), ¿qué efecto produce un aumento en la tasa de interés de los bonos (r) sobre la tenencia de dinero de un inversor con aversión al riesgo?",
        "options": [
            "Aumenta la demanda de dinero líquido de forma exponencial.",
            "Genera un efecto sustitución hacia los bonos que reduce la proporción de dinero líquido en la cartera (relación inversa entre demanda de dinero y tasa de interés).",
            "Provoca que el inversor venda todos sus activos financieros y compre inmuebles.",
            "No produce ningún efecto sobre la estructura de la cartera."
        ],
        "correct_index": 1,
        "explanation": "Al subir la tasa de interés, el rendimiento esperado de la cartera por unidad de riesgo aumenta, induciendo al inversor a aceptar más riesgo en bonos y recortar sus saldos monetarios líquidos ociosos."
    },
    {
        "id": "clasicos_12",
        "question": "¿En qué consiste la célebre 'Teoría de la Deflación por Deuda' (Debt-Deflation Theory) formulada por Irving Fisher en 1933 tras la Gran Depresión?",
        "options": [
            "En la propuesta de que el gobierno cancele todas las deudas tributarias de los agricultores.",
            "En la demostración de que cuando deudores sobreendeudados intentan pagar sus pasivos liquidando activos apresuradamente, la venta masiva derrumba los precios, haciendo que el valor real de la deuda remanente crezca en vez de bajar.",
            "En la abolición del patrón oro por decreto del presidente Herbert Hoover.",
            "En la teoría de que la deflación genera aumentos automáticos en el salario real de equilibrio."
        ],
        "correct_index": 1,
        "explanation": "Paradoja trágica de Fisher: 'cuanto más pagan los deudores, más deben'. Al liquidar bienes para cancelar deudas nominales, los precios caen más rápido de lo que se reduce la deuda; la deflación agrava la quiebra y hunde a la economía en depresión."
    },
    {
        "id": "clasicos_13",
        "question": "¿Cuál es el concepto conocido como la 'q de Tobin' introducido por James Tobin en 1969?",
        "options": [
            "El cociente entre el gasto público y los ingresos tributarios aduaneros.",
            "El ratio entre el valor de mercado bursátil de una empresa de capital y el costo de reposición física de sus activos productivos instalados: q = Valor bursátil / Costo de reposición.",
            "La tasa de inflación óptima que maximiza el señoreaje fiscal del Banco Central.",
            "La relación entre la oferta de dinero M1 y la base monetaria B."
        ],
        "correct_index": 1,
        "explanation": "La q de Tobin guía la inversión productiva: si q > 1, el mercado bursátil valora el capital de la firma por encima de lo que cuesta comprar maquinaria nueva, incentivando la inversión en nuevas plantas físicas."
    },
    {
        "id": "clasicos_14",
        "question": "¿Qué predice la teoría de la q de Tobin si la valoración de mercado de las acciones está muy por debajo de su costo de reposición (q < 1)?",
        "options": [
            "Las empresas construirán nuevas fábricas de inmediato para aprovechar las tasas de interés.",
            "La inversión física se deprime, ya que para las firmas es más barato adquirir capacidad instalada comprando acciones de empresas rivales en la bolsa que construir nuevas plantas físicas.",
            "El Banco Central decretará el cierre de los bancos comerciales insolventes.",
            "Las exportaciones manufactureras se duplicarán en el corto plazo."
        ],
        "correct_index": 1,
        "explanation": "Si q < 1, comprar capital usado a través de acciones bursátiles es más barato que comprar máquinas nuevas; la inversión productiva bruta se paraliza, afectando la demanda agregada."
    },
    {
        "id": "clasicos_15",
        "question": "¿Cómo concibe James Tobin la sustituibilidad entre el dinero y el capital físico en su modelo general de activos (enfoque de la Síntesis Neoclásica)?",
        "options": [
            "Los concibe como activos complementarios que siempre crecen juntos.",
            "Los concibe como activos competidores o sustitutos en la cartera de riqueza: si la rentabilidad del dinero sube, los inversores demandan más dinero y menos capital físico.",
            "Afirma que el dinero y el capital son idénticos bajo cualquier condición empírica.",
            "Sostiene que el capital físico no rinde ningún flujo de beneficios reales."
        ],
        "correct_index": 1,
        "explanation": "En el modelo de carteras de Tobin para economías avanzadas, el dinero compite con el capital. Si el dinero es muy atractivo o rinde altos intereses reales, desplaza a la inversión en capital productivo (contraste con McKinnon)."
    },
    {
        "id": "clasicos_16",
        "question": "¿Qué es el 'Efecto Pigou' (o Efecto de Saldos Reales) formulado por Arthur Cecil Pigou en 1943?",
        "options": [
            "La teoría de que los impuestos al tabaco reducen el consumo de cigarrillos.",
            "El mecanismo mediante el cual una caída en el nivel de precios eleva el valor real de la riqueza monetaria líquida del público (M/P sube), estimulando el consumo autónomo y restaurando el pleno empleo sin necesidad de política fiscal.",
            "La propuesta de indexar los salarios a la inflación pasada cada seis meses.",
            "El colapso del multiplicador del comercio exterior ante una devaluación."
        ],
        "correct_index": 1,
        "explanation": "Intento clásico de refutar la trampa de liquidez keynesiana: Pigou argumenta que si los precios caen lo suficiente, los saldos monetarios reales se vuelven tan valiosos que la riqueza neta del público sube, reactivando el consumo y el empleo."
    },
    {
        "id": "clasicos_17",
        "question": "¿Por qué Michal Kalecki e Irving Fisher descalificaron la efectividad práctica del Efecto Pigou en economías reales?",
        "options": [
            "Porque la mayoría del dinero no es dinero externo emitido por el Estado (outside money), sino dinero de crédito bancario interno (inside money); la deflación arruina a los deudores mucho más de lo que beneficia a los acreedores.",
            "Porque Pigou no había publicado su tesis en una revista estadounidense.",
            "Porque los precios nunca pueden bajar en ninguna economía del mundo.",
            "Porque el consumo de las familias no depende de la riqueza acumulada."
        ],
        "correct_index": 0,
        "explanation": "El efecto riqueza del dinero neto estatal es diminuto frente al volumen gigantesco de deuda privada interna. La caída de precios redistribuye riqueza hacia acreedores con baja propensión al gasto y quiebra a los deudores (Fisher), hundiendo la economía."
    },
    {
        "id": "clasicos_18",
        "question": "¿En qué consiste la teoría de los intermediarios financieros desarrollada por James Tobin y William Brainard (1963)?",
        "options": [
            "En que los bancos comerciales son los únicos intermediarios financieros capaces de operar en el mercado.",
            "En que los bancos comerciales son solo una especie dentro de un género más amplio de intermediarios financieros (fondos, mutuales, compañías de seguros) que compiten emitiendo pasivos y comprando activos según rendimientos relativos.",
            "En la propuesta de eliminar la intermediación bancaria y sustituirla por préstamos directos entre familias.",
            "En la exigencia de que todos los préstamos bancarios se cancelen en menos de 90 días."
        ],
        "correct_index": 1,
        "explanation": "Enfoque de la nueva visión bancaria: el sistema bancario comercial no tiene un monopolio místico; compite con otros intermediarios financieros en una estructura compleja de cartera basada en primas de riesgo y sustituibilidad de activos."
    },
    {
        "id": "clasicos_19",
        "question": "¿Qué distinción establece Arthur C. Pigou entre los costos privados y los costos sociales en su economía del bienestar?",
        "options": [
            "No establece ninguna distinción analítica relevante.",
            "Demuestra que cuando existen externalidades negativas (como la contaminación o las corridas bancarias), el costo social supera al costo privado, justificando impuestos pigouvianos o regulación estatal.",
            "Afirma que el Estado debe financiar todos los costos privados de las empresas industriales.",
            "Sostiene que el bienestar social se maximiza suprimiendo la propiedad privada."
        ],
        "correct_index": 1,
        "explanation": "Aporte clásico de Pigou: las fallas de mercado y externalidades generan una brecha entre beneficios privados y sociales, fundamentando la intervención regulatoria y tributaria del Estado."
    },
    {
        "id": "clasicos_20",
        "question": "¿Cuál es la síntesis de la evolución histórica de la teoría de la demanda de dinero analizada exhaustivamente en el programa?",
        "options": [
            "La teoría del dinero no ha cambiado desde Aristóteles hasta nuestros días.",
            "Evolucionó desde un enfoque mecánico transaccional de pagos (Fisher), pasó a la decisión microeconómica de saldos de caja (Cambridge) y preferencia por la liquidez (Keynes), fue microfundamentada en inventarios y carteras (Baumol-Tobin), y reformulada como activo de capital estable (Friedman).",
            "La teoría monetaria fue reemplazada en su totalidad por la teoría de la relatividad de Einstein.",
            "El análisis de la demanda de dinero demostró que el dinero físico es el único activo que no sufre depreciación en el tiempo."
        ],
        "correct_index": 1,
        "explanation": "Recorrido doctrinal completo de la materia: Fisher (M·V=P·T) $\\rightarrow$ Cambridge (M^d=kPY) $\\rightarrow$ Keynes (L1+L2) $\\rightarrow$ Baumol-Tobin (inventarios y selección de cartera) $\\rightarrow$ Friedman (reformulación como activo estable en la riqueza total) $\\rightarrow$ Cagan (huida en hiperinflaciones)."
    }
]

print(f"Cargadas las 100 preguntas de la Parte 2 (Werning, Shackle, Zuleta, Johnson, Clásicos-Poskeynesianos).")


# generate_university_database.py
# -*- coding: utf-8 -*-
import json
import os

print("Generating exhaustive university-grade database...")

# Transversal Topics Definition with exam-oriented descriptions
topics_data = [
    {
        "id": "t1_definicion_dinero",
        "name": "1. Definición y Naturaleza del Dinero",
        "description": "Naturaleza de los activos monetarios: ¿qué es dinero? ¿Es una variable exógena controlada por el banco central o endógena creada por el crédito bancario? Debate empírico vs teórico (M1, M2, crédito comercial y liquidez general)."
    },
    {
        "id": "t2_demanda_dinero",
        "name": "2. Demanda de Dinero y Preferencia por la Liquidez",
        "description": "Fundamentos microeconómicos y motivos de tenencia: transacción, precaución, especulación y activo de capital en la riqueza total. Sensibilidad a la tasa de interés, trampa de liquidez y debate crucial sobre la estabilidad empírica de la función."
    },
    {
        "id": "t3_inflacion",
        "name": "3. Causas y Mecanismos de la Inflación",
        "description": "¿Cuál es la causa motriz de la inflación? Confrontación doctrinaria: exceso de emisión monetaria (Monetarismo), conflicto distributivo y espiral salarios-precios (Lorenzoni-Werning), estrangulamientos sectoriales y dinero pasivo (Estructuralismo), o déficit fiscal y señoreaje (Finanzas Públicas)."
    },
    {
        "id": "t4_sistema_bancario",
        "name": "4. Sistema Bancario, Intermediación y Creación de Crédito",
        "description": "El rol macroeconómico de los bancos: ¿son intermediarios neutros de fondos prestables, creadores de depósitos ex nihilo al otorgar préstamos, o fuentes activas de aceleración financiera por asimetría de información y costos de agencia?"
    },
    {
        "id": "t5_crisis_fluctuaciones",
        "name": "5. Crisis Financieras, Pánicos y Fluctuaciones",
        "description": "¿Qué origina las depresiones y los ciclos económicos? Choques de oferta monetaria, quiebra de la intermediación y destrucción de información crediticia (Bernanke), corridas bancarias y shadow banking, deflación por deuda o colapso de los espíritus animales bajo incertidumbre radical."
    },
    {
        "id": "t6_politica_monetaria",
        "name": "6. Política Monetaria: Reglas vs Discreción y Efectividad",
        "description": "¿Debe intervenir el Banco Central con discrecionalidad anticíclica o atarse a reglas fijas creíbles? Regla del k% de Friedman, ineficacia de la política anticipada (Lucas-Sargent), inconsistencia temporal (Kydland-Prescott) y el rol de prestamista de última instancia (Bagehot/Bernanke)."
    },
    {
        "id": "t7_expectativas_metodologia",
        "name": "7. Expectativas, Incertidumbre y Metodología",
        "description": "Epistemología de la ciencia económica: instrumentalismo positivo del 'como si' (Friedman), expectativas adaptativas, expectativas racionales y vaciado de mercados (Lucas), versus incertidumbre radical incalculable, sorpresa potencial y tiempo histórico (Keynes y Shackle)."
    },
    {
        "id": "t8_represion_desarrollo",
        "name": "8. Represión Financiera y Desarrollo Económico",
        "description": "Efecto de las regulaciones financieras en países en desarrollo: techos a tasas de interés, encajes confiscatorios, crédito dirigido e impuesto inflacionario. La hipótesis de complementariedad dinero-capital de McKinnon y la necesidad de liberalización financiera."
    }
]

# We will generate comprehensive, academic entries for each economist
# with exact details for university exams.
economists_data = [
    {
        "id": "friedman",
        "name": "Milton Friedman",
        "school": "Escuela de Chicago / Monetarismo Moderno",
        "epoch": "Mediados del Siglo XX (décadas de 1950 a 1970)",
        "context": "Líder indiscutido de la Escuela de Chicago y artífice de la Contrarrevolución Monetarista que desafió y desplazó a la ortodoxia keynesiana de posguerra. Premio Nobel de Economía en 1976. Sus obras centrales en el programa son 'La Metodología de la Economía Positiva' (1953), 'La Reformulación de la Teoría Cuantitativa del Dinero' (1956) y 'A Monetary History of the United States, 1867-1960' (1963, junto a Anna J. Schwartz).",
        "primary_texts": ["Facu 100 (Metodología de la Economía Positiva)", "Facu 96 (Antonio Argandoña - Milton Friedman)", "Facu 64 (Harry Johnson)", "Facu 59 (Argandoña - Definición de Dinero)", "Facu 108 (Desde Keynes hasta Lucas)"],
        "stances": {
            "t1_definicion_dinero": """• TESIS CENTRAL Y CRITERIO DE DEMARCACIÓN:
Friedman rechaza cualquier intento de definir el dinero a priori en base a propiedades filosóficas, jurídicas o intrínsecas. En su obra metodológica de 1953 y en sus investigaciones empíricas junto a Anna Schwartz (1970), sostiene un criterio estrictamente instrumental y pragmático: el concepto adecuado de dinero es aquel agregado estadístico cuya relación con variables macroeconómicas clave —especialmente el ingreso nacional nominal— resulte más estable, regular y con mayor capacidad predictiva.

• AGREGADO DEFENDIDO (M2):
Tras examinar extensas series históricas estadounidenses, Friedman y Schwartz concluyen que el agregado óptimo es M2, definido como:
M2 = Circulante en poder del público + Depósitos a la vista en bancos comerciales + Depósitos a plazo en bancos comerciales (excluyendo certificados negociables de gran cuantía emitidos a partir de 1961).
Descartan M1 porque consideran que los depósitos a plazo en la banca comercial son sustitutos casi perfectos de los depósitos a la vista en la demanda de saldos monetarios del público.

• CONTRASTE PARA EXAMEN:
Frente al enfoque de la Currency School (que solo consideraba dinero al oro y los billetes) y frente a los enfoques de liquidez amplia del Informe Radcliffe (1959) y Gurley-Shaw (que diluían el dinero en un mar de sustitutos no bancarios), Friedman demuestra que M2 mantiene un comportamiento empíricamente gobernable por la autoridad monetaria a través del control de la base monetaria.""",

            "t2_demanda_dinero": """• TESIS CENTRAL: LA REFORMULACIÓN MONETARISTA (1956):
Friedman no formula una teoría de los precios ni de la producción, sino estrictamente una teoría de la DEMANDA DE DINERO. Trata al dinero no como un simple medio mecánico de cambio (como Fisher), sino como un ACTIVO DE CAPITAL DURADERO que rinde un flujo de servicios de liquidez, seguridad y conveniencia, integrado dentro de la cartera general de riqueza de los agentes.

• FORMALIZACIÓN Y VARIABLES DETERMINANTES:
La demanda de saldos monetarios reales se expresa como:
(M / P)^d = f(Y_p, w, r_m, r_b, r_e, π^e, u)
Donde las variables son:
1. Riqueza Total (W), aproximada por el Ingreso Permanente (Y_p): Es la restricción presupuestaria de largo plazo. La elasticidad-ingreso permanente de la demanda de dinero es positiva y ligeramente superior a la unidad (trata al dinero como un bien de lujo).
2. Proporción de Riqueza Humana a No Humana (w): La riqueza humana (capacidad de trabajo futura) es ilíquida; a mayor proporción de riqueza humana, mayor necesidad de mantener saldos monetarios líquidos de reserva.
3. Rendimiento Propio del Dinero (r_m): Intereses explícitos o implícitos que devengan los depósitos.
4. Rendimiento Esperado de Activos Financieros Alternativos: Tasa de interés de los bonos (r_b) y rendimiento esperado de las acciones (r_e).
5. Rendimiento de los Bienes Físicos / Inflación Esperada (π^e): En economías con inflación, los bienes reales son el activo sustituto del dinero; un alza en la inflación esperada encarece el costo de oportunidad de tener dinero y reduce su demanda.
6. Variables Institucionales y Preferencias (u).

• EL POSTULADO CRUCIAL: ESTABILIDAD DE LA FUNCIÓN:
Para Friedman, la velocidad de circulación del dinero (V) NO es una constante física fija como creía la versión clásica simplificada, pero la FUNCIÓN de demanda de dinero es NOTABLEMENTE ESTABLE en el tiempo. Como la demanda de saldos reales no experimenta desplazamientos erráticos ni caprichosos (no existen 'trampas de liquidez' keynesianas permanentes), cualquier variación no explicada en el ingreso nominal proviene de fluctuaciones en la oferta monetaria generadas por el Banco Central.""",

            "t3_inflacion": """• TESIS CENTRAL:
'La inflación es siempre y en todo lugar un fenómeno monetario, en el sentido de que solo es y puede ser producida por un aumento de la cantidad de dinero más rápido que el de la producción'.

• MECANISMO DE TRANSMISIÓN:
1. El Banco Central expande la oferta de dinero (M) por encima de la tasa de crecimiento del producto potencial real (Y).
2. Los agentes económicos se encuentran con más saldos monetarios reales (M/P) de los que desean mantener según su función estable de demanda de dinero.
3. Dado que no desean atesorar ese excedente líquido, intentan desprenderse de él aumentando su gasto en bienes de consumo, servicios y activos financieros y reales.
4. Como la economía no puede incrementar instantáneamente la capacidad productiva física más allá del pleno empleo, este exceso de demanda agregada presiona directamente al alza el nivel general de precios (P).
5. Los precios continúan subiendo hasta que los saldos monetarios reales (M/P) se reducen exactamente al nivel deseado por el público, restableciendo el equilibrio.

• REFUTACIÓN DE TEORÍAS ALTERNATIVAS (CLAVE PARA EXAMEN):
Friedman rechaza categóricamente las explicaciones de inflación de costos, inflación por puja salarial o inflación estructural:
- Los sindicatos pueden elevar el salario relativo de sus afiliados, pero si la masa monetaria no se expande, esto genera desempleo en otros sectores o caída de otros precios, jamás inflación continua.
- Las subas del petróleo o monopolios generan un cambio de precios relativos de una sola vez, pero no pueden causar un aumento sostenido y generalizado del nivel de precios.
- Si hay inflación sostenida, es porque el gobierno y el Banco Central convalidaron monetariamente esas presiones emitiendo dinero para evitar el desempleo transitorio.""",

            "t4_sistema_bancario": """• ROL DE LA BANCA EN EL MONETARISMO:
Friedman concibe al sistema bancario dentro del esquema del multiplicador monetario tradicional. Los bancos comerciales son intermediarios financieros que captan depósitos y otorgan crédito bajo un régimen de reserva fraccionaria.

• EL MULTIPLICADOR Y LA TRANSMISIÓN:
La oferta monetaria total (M) es el producto de la base monetaria emitida por el Banco Central (B = Circulante + Reservas bancarias) y el multiplicador bancario (m):
M = m · B, donde m = (c + 1) / (c + r), con c = relación circulante/depósitos y r = coeficiente de encaje bancario.
Aunque reconoce que las decisiones de los bancos comerciales sobre encajes excedentes y las decisiones del público sobre la tenencia de efectivo pueden hacer fluctuar el multiplicador a corto plazo, insiste en que el Banco Central posee herramientas suficientes (operaciones de mercado abierto, tasa de descuento y encajes legales) para dominar y neutralizar estas fluctuaciones, controlando la masa monetaria final.""",

            "t5_crisis_fluctuaciones": """• REINTERPRETACIÓN DE LA GRAN DEPRESIÓN DE 1929:
En su monumental investigación con Anna Schwartz ('A Monetary History of the United States', 1963), Friedman desmiente la narrativa keynesiana de que la crisis de los años 30 demostró la inestabilidad intrínseca de la inversión privada y el fracaso del capitalismo de libre mercado.

• DIAGNÓSTICO HISTÓRICO:
La Gran Depresión fue causada y agravada por la desastrosa gestión de la Reserva Federal (Fed). Entre 1929 y 1933, la Fed permitió que la oferta monetaria de los Estados Unidos se contrajera en más de un tercio (-33%).
La Fed se negó a cumplir su función de prestamista de última instancia ante las olas sucesivas de pánicos bancarios, permitiendo la quiebra de miles de bancos comerciales solventes. Al colapsar los depósitos y dispararse la preferencia del público por el billete físico, el multiplicador monetario y la cantidad total de dinero se desplomaron, provocando una catástrofe deflacionaria que arrastró al producto real y al empleo.

• CONCLUSIÓN DOCTRINAL:
Las grandes fluctuaciones económicas no son generadas por la inestabilidad inherente del sector privado, sino por shocks monetarios exógenos causados por las intervenciones erráticas del propio Estado.""",

            "t6_politica_monetaria": """• CURVA DE PHILLIPS Y TASA NATURAL DE DESEMPLEO (1968):
Friedman demuele el postulado keynesiano de que existe un dilema estable y explotable entre inflación y desempleo.
- A corto plazo: Una expansión monetaria imprevista puede reducir transitoriamente el desempleo por debajo de su nivel de equilibrio porque los trabajadores sufren 'ilusión monetaria' o forman expectativas adaptativas (los salarios nominales suben, los empresarios ven caer el salario real y contratan más, mientras los trabajadores creen erróneamente que su salario real subió).
- A largo plazo: Los trabajadores perciben que los precios de los bienes aumentaron, corrigen sus expectativas de inflación y exigen aumentos salariales compensatorios. Los costos de las empresas suben, los despidos se reanudan y el desempleo retorna inexorablemente a la TASA NATURAL DE DESEMPLEO (u_n).
- Consecuencia: La Curva de Phillips es VERTICAL a largo plazo. Intentar mantener el desempleo permanentemente por debajo de la tasa natural mediante emisión solo genera una espiral de inflación acelerada.

• LA REGLA MONETARIA DEL k%:
Debido a la existencia de rezagos temporales largos y variables (lags de reconocimiento, de implementación y de impacto en la economía real), el activismo monetario discrecional ('fine-tuning') actúa de manera procíclica y desestabiliza la economía.
Prescripción: Abolir la discrecionalidad de los bancos centrales y someterlos a una regla constitucional rígida: incrementar la oferta monetaria a una tasa fija y constante anual (entre el 3% y el 5%), alineada con el crecimiento del producto potencial de largo plazo.""",

            "t7_expectativas_metodologia": """• LA METODOLOGÍA DE LA ECONOMÍA POSITIVA (1953):
Friedman establece los cánones epistemológicos del Instrumentalismo Positivo en economía:
1. Dicotomía: Ciencia positiva (lo que es, independiente de juicios morales) vs Ciencia normativa (lo que debe ser, juicios de valor).
2. El Fin de la Teoría: El objetivo de una ciencia positiva es construir hipótesis capaces de generar predicciones empíricas válidas y precisas sobre fenómenos aún no observados.
3. El Rechazo al Realismo de los Supuestos: Es un error metodológico fatal juzgar la validez de una teoría por el realismo descriptivo de sus premisas. Todos los supuestos son irreales porque abstraen la infinita complejidad de la realidad. De hecho, 'cuanto más significativa es una teoría, más irrealistas son sus supuestos', pues logra explicar mucho con poco.
4. El Postulado del 'Como Si' (As If): Los modelos no pretenden describir el proceso psicológico consciente de los actores, sino predecir su comportamiento agregado. Los agentes actúan 'como si' maximizaran funciones matemáticas complejas (ejemplos: el jugador experto de billar que tira como si conociera las leyes de la cinemática, o las hojas del árbol que crecen como si optimizaran la captación solar).
5. En macroeconomía formula las expectativas adaptativas: los agentes corrigen sus previsiones en base a los errores pasados ponderados exponencialmente.""",

            "t8_represion_desarrollo": """• POSICIÓN DOCTRINAL:
Aunque Friedman concentró sus investigaciones empíricas en economías industriales maduras (EE.UU. y Gran Bretaña), su defensa radical de la libre determinación de precios y su condena a los controles estatales de precios y tasas de interés constituyeron la inspiración teórica directa de las doctrinas de liberalización financiera (como las formuladas por McKinnon y Shaw). Sostiene que fijar techos artificiales a las tasas de interés distorsiona la asignación del capital y castiga el ahorro voluntario."""
        }
    },
    {
        "id": "keynes",
        "name": "John Maynard Keynes",
        "school": "Escuela de Cambridge / Teoría General Keynesiana",
        "epoch": "Década de 1930 (Gran Depresión de 1929 / Publicación de la Teoría General en 1936)",
        "context": "Figura cumbre de la ciencia económica del siglo XX. Revolucionó el pensamiento económico al romper definitivamente con la ortodoxia clásica prekeynesiana y demostrar la posibilidad de equilibrios macroeconómicos con desempleo involuntario masivo y persistente. Sus textos analizados en el programa son 'The General Theory of Employment, Interest and Money' (1936), discutido en profundidad en 'Desde Keynes hasta Lucas' (Maya Muñoz), 'Revolución y contrarrevolución' (Harry Johnson) y 'Demanda de dinero' (Chaves Barea).",
        "primary_texts": ["Facu 108 (Desde Keynes hasta Lucas)", "Facu 97 (Demanda de Dinero)", "Facu 64 (Harry Johnson)", "Facu 86 (Peter Earl / Shackle)"],
        "stances": {
            "t1_definicion_dinero": """• TESIS CENTRAL: EL DINERO COMO ACTIVO LÍQUIDO FUNDAMENTAL:
Keynes rompe con la noción clásica del dinero como un simple 'velo' neutro que solo sirve para agilizar el trueque de bienes reales. Para Keynes, el dinero es el activo líquido por excelencia (M1: circulante y depósitos a la vista) que posee una propiedad única: es el eslabón institucional que conecta el presente con un futuro incierto.
Su cualidad esencial es la LIQUIDEZ: la capacidad de convertirse inmediatamente en cualquier bien o cancelar obligaciones sin costo ni demora, otorgando seguridad en un mundo dominado por la incertidumbre.""",

            "t2_demanda_dinero": """• LA TEORÍA DE LA PREFERENCIA POR LA LIQUIDEZ:
La gran revolución analítica de Keynes consistió en incorporar el dinero dentro de la teoría de la elección de cartera bajo incertidumbre. Los agentes demandan saldos monetarios por tres motivos diferenciados:

1. Motivo Transacción (L_1): Para salvar la brecha temporal entre la percepción de ingresos y la realización de pagos cotidianos. Es función directa y positiva del nivel de ingreso corriente: L_1 = f(Y).
2. Motivo Precaución (L_1): Como reserva de seguridad para hacer frente a contingencias, imprevistos u oportunidades repentinas de compra ventajosa. También depende fundamentalmente del ingreso: L_1 = f(Y).
3. Motivo Especulación (L_2): La innovación teórica más trascendental de Keynes. Nace de la incertidumbre sobre la evolución futura de la tasa de interés de mercado. Los agentes eligen entre mantener dinero líquido (rendimiento nominal cero pero capital seguro) o adquirir bonos (que pagan un interés pero conllevan el riesgo de pérdida de capital si la tasa de interés sube y el precio del bono cae).
- Si la tasa de interés actual (r) es muy alta respecto a lo que el mercado considera 'normal', los agentes esperan que baje (los precios de los bonos subirán); por ende, prefieren comprar bonos y demandan poco dinero.
- Si la tasa de interés es muy baja, los agentes esperan que suba (los precios de los bonos se desplomarán); por ende, prefieren refugiarse en dinero líquido y la demanda de dinero aumenta fuertemente.
Por tanto, la demanda especulativa depende INVERSAMENTE de la tasa de interés: L_2 = f(r), con dL_2/dr < 0.

• LA FUNCIÓN TOTAL DE DEMANDA:
M^d = L_1(Y) + L_2(r)

• EL FENÓMENO DE LA TRAMPA DE LIQUIDEZ:
A una tasa de interés críticamente baja (cercana a cero), el público espera unánimemente que la tasa no pueda bajar más y solo pueda subir. En ese punto, el costo de oportunidad de mantener dinero es nulo y el riesgo de pérdida de capital en bonos es máximo: la curva de demanda de dinero se vuelve INFINITAMENTE ELÁSTICA (horizontal). Cualquier inyección monetaria del Banco Central es absorbida pasivamente por el público sin lograr reducir más la tasa de interés ni estimular el gasto.""",

            "t3_inflacion": """• RUPTURA CON LA TEORÍA CUANTITATIVA:
Keynes refuta la premisa clásica de que la emisión monetaria siempre causa inflación. Establece una distinción tajante según el nivel de utilización de la capacidad instalada:
1. En condiciones de desempleo involuntario y capacidad ociosa (Y < Y_pe): Una expansión de la demanda agregada (fiscal o monetaria) estimula la producción real y el empleo, mientras que los precios y salarios se mantienen relativamente estables. No hay inflación de demanda.
2. Inflación Verdadera (True Inflation): Ocurre ÚNICA Y EXCLUSIVAMENTE cuando la economía alcanza el PLENO EMPLEO FÍSICO de todos los factores productivos (Y = Y_pe). A partir de ese techo, la oferta agregada se vuelve completamente inelástica; cualquier aumento adicional del gasto no puede generar más producto real y se traduce íntegramente en un aumento proporcional de precios.
3. Reconoce además presiones de inflación de costos originadas por la puja de salarios nominales rígidos negociados por sindicatos.""",

            "t4_sistema_bancario": """• LA TASA DE INTERÉS COMO FENÓMENO MONETARIO:
Para los economistas clásicos, la tasa de interés era un fenómeno real: el precio que equilibraba el ahorro (abstinencia) con la inversión de capital productivo.
Keynes derriba esta doctrina: la tasa de interés es un fenómeno ESTRICTAMENTE MONETARIO. Es el precio que equilibra el deseo de retener riqueza en forma líquida (Preferencia por la Liquidez) con la cantidad de dinero existente creada por el sistema bancario y el Banco Central.
Los bancos no son simples intermediarios de un fondo previo de ahorro físico; influyen de forma decisiva en las condiciones de liquidez de la economía al alterar la oferta monetaria y las tasas de interés de corto plazo.""",

            "t5_crisis_fluctuaciones": """• CAUSA DE LAS RECESIONES Y DEPRESIONES:
Keynes niega que las crisis sean causadas por desajustes monetarios superficiales o por rigideces que el libre mercado corregiría solo si bajaran los salarios.
La causa profunda radica en la INESTABILIDAD DE LA INVERSIÓN PRIVADA, dominada por los 'Espíritus Animales' (Animal Spirits) de los empresarios y la Incertidumbre Radical sobre los rendimientos futuros del capital.

• EL MECANISMO DEL COLAPSO:
1. En una fase de auge, el optimismo ciego sobreestima la rentabilidad esperada del capital (Eficiencia Marginal del Capital, EMgK).
2. Ante cualquier perturbación o duda, la confianza empresarial se quiebra repentinamente; la EMgK se derrumba de forma abrupta.
3. Simultáneamente, el pánico dispara la Preferencia por la Liquidez del público y de los bancos, haciendo subir la tasa de interés o manteniéndola rígida.
4. Como la tasa de interés supera ahora a la reducida EMgK, la inversión privada colapsa.
5. A través del Multiplicador del Gasto, la caída de la inversión arrastra a la producción, al ingreso nacional y al empleo, hundiendo a la economía en un equilibrio persistente con desempleo involuntario del cual el mercado libre no puede salir por sí mismo.""",

            "t6_politica_monetaria": """• LÍMITES DE LA POLÍTICA MONETARIA Y PRIMACÍA FISCAL:
Keynes sostiene que la política monetaria es una herramienta asimétrica: puede ser útil para frenar un auge recalentado subiendo tasas, pero es profundamente INEFICAZ E IMPOTENTE para reactivar la economía en una depresión profunda (analogía célebre: 'se puede llevar el caballo al río, pero no se lo puede obligar a beber').
Razones de la impotencia monetaria:
1. Trampa de Liquidez: Las inyecciones monetarias no logran bajar la tasa de interés por debajo de su piso institucional.
2. Colapso de la EMgK: Aunque el Banco Central lograra abaratar el crédito, los empresarios no pedirán préstamos para invertir si sus expectativas de ventas futuras están destrozadas.
3. Prescripción: La única salida es la POLÍTICA FISCAL EXPANSIVA: el Estado debe asumir la 'socialización de la inversión', ejecutando obras públicas financiadas con déficit presupuestario para reinyectar demanda efectiva directa en el circuito económico.""",

            "t7_expectativas_metodologia": """• INCERTIDUMBRE RADICAL VERSUS RIESGO MATEMÁTICO:
En el famoso Capítulo 12 de la Teoría General, Keynes formula su visión metodológica sobre el futuro económico.
Rechaza tajantemente la aplicación del cálculo de probabilidades neoclásico para decisiones de inversión de largo plazo. El futuro económico no es riesgoso en el sentido de una ruleta de casino con probabilidades conocidas; es GENUINAMENTE INCIERTO: 'Simplemente, no lo sabemos' (Keynes, 1937).
Las expectativas no se forman mediante optimización intertemporal perfecta, sino a través de 'convenciones precarias', imitación del comportamiento de la masa (concurso de belleza keynesiano) y estados de confianza psicológica sumamente frágiles y volátiles.""",

            "t8_represion_desarrollo": """• ALCANCE ANALÍTICO:
[No aborda este tema puntualmente en los textos de la cátedra].
El marco analítico de Keynes fue diseñado específicamente para dar respuesta a la Gran Depresión en economías industriales maduras con mercados financieros sofisticados y exceso de capacidad ociosa (Reino Unido y Estados Unidos), y no para problemas de subdesarrollo financiero, dualismo estructural o escasez crónica de capital en el Tercer Mundo."""
        }
    },
    {
        "id": "lucas",
        "name": "Robert Lucas Jr. (& Sargent / Wallace)",
        "school": "Nueva Macroeconomía Clásica (Escuela de Expectativas Racionales)",
        "epoch": "Décadas de 1970 a 1980",
        "context": "Líder de la segunda gran contrarrevolución contra la síntesis keynesiana. Premio Nobel de Economía en 1995. Transformó radicalmente la metodología macroeconómica al exigir microfundamentos rigurosos de equilibrio general walrasiano, vaciado continuo de mercados y la Hipótesis de Expectativas Racionales. Obras de referencia: 'Expectations and the Neutrality of Money' (1972) y 'Econometric Policy Evaluation: A Critique' (1976), analizadas detalladamente en 'Desde Keynes hasta Lucas' (Maya Muñoz).",
        "primary_texts": ["Facu 108 (Desde Keynes hasta Lucas)", "Facu 96 (Antonio Argandoña - Milton Friedman)", "Facu 100 (Metodología Positiva)"],
        "stances": {
            "t1_definicion_dinero": """• ENFOQUE TEÓRICO FORMAL:
Lucas y los nuevos clásicos modelan el dinero de manera puramente abstracta y formal en modelos microfundamentados intertemporales, típicamente mediante restricciones de 'dinero por adelantado' (Cash-in-Advance models de Clower/Lucas) o introduciendo los saldos reales directamente en la función de utilidad de los hogares (Money-in-the-Utility function de Sidrauski).
El dinero es concebido como el medio de cambio fiduciario provisto exógenamente por la autoridad monetaria para facilitar el intercambio sin fricciones en mercados perfectamente competitivos.""",

            "t2_demanda_dinero": """• MICROFUNDAMENTACIÓN INTERTEMPORAL:
Rechazan de plano las funciones de demanda de dinero agregadas 'ad-hoc' (como las estimadas empíricamente por los keynesianos o monetaristas tradicionales).
Para Lucas, la tenencia de dinero debe derivarse estrictamente de las condiciones de primer orden de agentes maximizadores que resuelven un problema de optimización intertemporal bajo restricciones de liquidez y presupuesto. La demanda de dinero responde a la tasa de preferencia intertemporal, los precios relativos esperados y la tasa de interés nominal como costo de oportunidad de mantener liquidez en vez de activos de capital acumulable.""",

            "t3_inflacion": """• INFLACIÓN PURA Y NEUTRALIDAD ESTRICTA:
La inflación es en todo momento el reflejo directo de la tasa de expansión de la oferta monetaria.
Bajo la hipótesis de expectativas racionales, si la emisión de dinero es ANTICIPADA o sistemática, los agentes incorporan instantáneamente esa información en sus decisiones: ajustan de inmediato sus demandas de salarios y precios nominales en la misma proporción que la emisión esperada.
Resultado: La emisión monetaria anticipada se traslada 1:1 al nivel general de precios sin generar el más mínimo incremento transitorio en la producción real ni en el empleo. La neutralidad del dinero se cumple tanto a largo plazo como a CORTO PLAZO frente a políticas conocidas.""",

            "t4_sistema_bancario": """• INTERMEDIARIOS NEUTROS EN MODELOS WALRASIANOS:
En los modelos nuevo-clásicos estándar de Lucas, Sargent y Prescott, el sistema bancario se modela como un conjunto de intermediarios financieros perfectamente competitivos sin fricciones informacionales de relevancia agregada.
Operan bajo las condiciones del teorema Modigliani-Miller a nivel macroeconómico: la estructura del sistema financiero y las formas de financiamiento bancario no alteran las decisiones reales de ahorro e inversión de equilibrio general, ya que los mercados financieros son completos y se vacían continuamente.""",

            "t5_crisis_fluctuaciones": """• ORIGEN DE LOS CICLOS Y LA CURVA DE OFERTA DE LUCAS:
Lucas rechaza tanto las fallas de demanda keynesianas como los rezagos adaptativos de Friedman. En su famoso modelo de las islas (1972), formula la Curva de Oferta Agregada de Lucas:
y_t = y_n + α (P_t - E_{t-1}[P_t])
Donde y_n es el producto natural y (P_t - E_{t-1}[P_t]) es la 'sorpresa de precios'.

• MECANISMO DE LA 'SORPRESA MONETARIA':
1. La economía está fragmentada en mercados o 'islas' con información imperfecta y dispersa.
2. Cada productor observa inmediatamente el precio nominal de su propio bien, pero no puede observar instantáneamente el nivel general de precios de toda la economía.
3. Si el Banco Central ejecuta una emisión monetaria NO ANTICIPADA (un shock estocástico imprevisto), el precio nominal del bien sube.
4. El productor enfrenta un problema de 'extracción de señales': confunde el shock inflacionario general con un aumento en la demanda real de su propio producto y eleva transitoriamente su producción y horas trabajadas.
5. En cuanto se difunde la información y los agentes descubren que todos los precios subieron por igual, corrigen su error y la producción retorna de inmediato a su nivel natural.
Las fluctuaciones reales solo pueden ser provocadas por shocks no anticipados (sorpresas) o, en la versión posterior de Kydland y Prescott (Teoría de Ciclos Reales), por shocks tecnológicos reales de productividad.""",

            "t6_politica_monetaria": """• LA PROPOSICIÓN DE INEFICACIA DE LA POLÍTICA (PIP):
Formulada por Thomas Sargent y Neil Wallace (1975) en el marco lucasiano:
Cualquier regla de política monetaria sistemática, previsible, anunciada o basada en retroalimentación anticíclica (por ejemplo, 'expandir dinero cuando el desempleo sube') es TOTALMENTE INEFICAZ para estabilizar el producto real o el empleo, incluso en el muy corto plazo. Los agentes racionales anticipan la reacción del banco central y neutralizan sus efectos reales en los precios. Solo las políticas arbitrarias y erráticas (sorpresas) tienen efectos reales, pero generan volatilidad dañina.

• LA CRÍTICA DE LUCAS (1976 - CLAVE DE EXAMEN):
Es una de las contribuciones metodológicas más demoledoras del siglo XX. Lucas demuestra la invalidez teórica de utilizar los grandes modelos macroeconométricos tradicionales (como los de la síntesis keynesiana) para evaluar o simular los efectos de cambios en la política económica.
Argumento: Los parámetros estimados en esos modelos (como la propensión a consumir, la elasticidad de la demanda de dinero o la pendiente de la curva de Phillips) NO son invariantes ni estructurales; reflejan simplemente las reglas óptimas que adoptaron los agentes racionales bajo el régimen de política que rigió en el pasado. Cuando el gobierno anuncia un cambio de régimen o de política, los agentes racionales modifican inmediatamente sus expectativas y sus reglas de comportamiento, alterando todos los parámetros del modelo. Por ende, las predicciones econométricas basadas en datos históricos quedan completamente falseadas.

• INCONSISTENCIA TEMPORAL (KYDLAND Y PRESCOTT 1977):
Los gobiernos con discrecionalidad sufren un problema de credibilidad: tienen incentivos a prometer inflación baja y luego generar una sorpresa inflacionaria para reducir el desempleo. Los agentes racionales descuentan esta trampa, eliminando la ganancia de empleo y fijando un 'sesgo inflacionario' permanente.
Solución: Reglas constitucionales rígidas y bancos centrales independientes y conservadores.""",

            "t7_expectativas_metodologia": """• LA HIPÓTESIS DE EXPECTATIVAS RACIONALES:
Formulada originalmente por John Muth (1961) en microeconomía e introducida por Lucas en la macroeconomía general:
1. Definición: Las expectativas subjetivas de los agentes económicos sobre las variables futuras coinciden con la esperanza matemática condicional del verdadero modelo económico objetivo que genera los datos:
E_{t-1}[X_t] = E[X_t | I_{t-1}]
Donde I_{t-1} es toda la información disponible en el período anterior.
2. Propiedades: Los agentes no cometen errores sistemáticos ni correlacionados. Los errores de pronóstico son pura sorpresa estocástica (ruido blanco ortogonal con media cero).
3. Ruptura con las expectativas adaptativas de Friedman: Bajo expectativas adaptativas, los agentes miran hacia el pasado y cometen errores sistemáticos persistentes durante períodos de aceleración inflacionaria. Bajo expectativas racionales, los agentes miran hacia adelante (*forward-looking*) e incorporan anuncios creíbles de política de forma instantánea.""",

            "t8_represion_desarrollo": """• ALCANCE ANALÍTICO:
[No aborda este tema puntualmente en los textos del curso].
La escuela nuevo-clásica se enfocó exclusivamente en la crítica metodológica de la macroeconometría de países desarrollados y en la formalización de modelos dinámicos estocásticos de equilibrio general (DSGE)."""
        }
    },
    {
        "id": "bernanke",
        "name": "Ben S. Bernanke (& Gertler / Gilchrist)",
        "school": "Nueva Economía Keynesiana / Escuela del Canal del Crédito",
        "epoch": "Décadas de 1980 a 2020s (Premio Nobel de Economía en 2022)",
        "context": "Presidente de la Reserva Federal durante la Gran Crisis Financiera de 2008 y galardonado con el Premio Nobel de Economía en 2022 junto a Douglas Diamond y Philip Dybvig. Su conferencia Nobel 'Banking, Credit, and Economic Fluctuations' (diciembre de 2022) y sus investigaciones previas ('Nonmonetary Effects of the Financial Crisis in the Propagation of the Great Depression', 1983; Bernanke, Gertler y Gilchrist, 1999) revolucionaron la comprensión del sistema bancario, superando la visión del dinero como simple agregado cuantitativo.",
        "primary_texts": ["Facu 102 (Nobel Prize Lecture: Banking, Credit, and Economic Fluctuations)"],
        "stances": {
            "t1_definicion_dinero": """• SUPERACIÓN DE LOS AGREGADOS MONETARIOS ESTRECHOS:
Bernanke supera la fijación clásica y monetarista en la masa monetaria líquida (M1 o M2). Enfatiza que en los sistemas financieros contemporáneos, la variable crítica para la actividad real no es la cantidad física de billetes, sino el VOLUMEN TOTAL DE CRÉDITO EFECTIVAMENTE DISPONIBLE y las condiciones de liquidez en los mercados mayoristas no bancarios (papeles comerciales, repos y deuda colateralizada en la banca en la sombra o shadow banking).""",

            "t2_demanda_dinero": """• DEL MERCADO MONETARIO AL MERCADO DE FONDOS PRESTABLES:
[No formula una teoría aislada de demanda de saldos monetarios convencionales].
Su investigación traslada el foco desde la demanda de dinero por motivos de liquidez hacia la DEMANDA Y OFERTA DE FONDOS DE FINANCIAMIENTO EXTERNO. Analiza cómo las empresas y los hogares demandan crédito bancario y cómo esa demanda queda racionada o encarecida cuando el colateral disponible se deteriora.""",

            "t3_inflacion": """• MARCO NUEVO KEYNESIANO Y RIESGO DE BURBUJAS CREDITICIAS:
Adopta el marco de Metas de Inflación (Inflation Targeting) con curvas de Phillips Nuevo Keynesianas basadas en costos marginales y fijación escalonada de precios (Calvo).
Sin embargo, su aporte específico radica en alertar que una estabilidad aparente de precios de bienes y servicios puede convivir con una peligrosa acumulación de desequilibrios crediticios y burbujas especulativas en el precio de los activos (vivienda, acciones), que al estallar amenazan con paralizar el sistema bancario y desatar deflaciones severas.""",

            "t4_sistema_bancario": """• EL SISTEMA BANCARIO NO ES UN VELO NEUTRAL:
Pilar fundamental de la teoría de Bernanke: Los bancos comerciales y los intermediarios financieros NO son simples conductos pasivos por donde fluyen fondos prestables.
1. Asimetría de Información y Costos de Agencia: El mercado de crédito está plagado de problemas de selección adversa (los malos prestatarios son los más ansiosos por pedir crédito) y riesgo moral (incentivo a desviar fondos a proyectos de alto riesgo una vez obtenido el préstamo).
2. La Función Social del Banco: Los bancos comerciales resuelven estas fallas mediante la especialización en la evaluación rigurosa de proyectos, la fijación de contratos de crédito con colateral y el monitoreo continuo de los deudores a través de relaciones de largo plazo (relationship lending).
3. Transformación de Vencimientos y Vulnerabilidad (Diamond-Dybvig 1983): Los bancos transforman pasivos líquidos a corto plazo (depósitos exigibles de inmediato) en activos ilíquidos a largo plazo (préstamos productivos e hipotecas). Esta función es vital para la economía pero los hace inherentemente vulnerables a PÁNICOS Y CORRIDAS BANCARIAS que pueden destruir entidades solventes.""",

            "t5_crisis_fluctuaciones": """• EL MECANISMO DEL ACELERADOR FINANCIERO (Bernanke, Gertler y Gilchrist 1999):
1. Prima de Financiamiento Externo (External Finance Premium): Es el sobrecosto o margen que una empresa debe pagar por solicitar fondos a terceros en comparación con el costo de oportunidad de usar sus propios fondos internos. Esta prima compensa a los prestamistas por la asimetría de información y varía INVERSAMENTE con la riqueza neta y el valor del colateral del prestatario.
2. Amplificación Cíclica: En una recesión, la caída en las ventas y en el precio de los activos deteriora los balances de empresas y familias. Al reducirse el colateral, la prima de financiamiento externo se dispara, encareciendo y racionando drásticamente el crédito. Esto obliga a recortar la inversión y el empleo, profundizando la caída del precio de los activos en una espiral viciosa descendente que propaga y amplifica shocks moderados.

• REINTERPRETACIÓN Y CORRECCIÓN A FRIEDMAN SOBRE 1929 (Bernanke 1983 - CLAVE DE EXAMEN):
Bernanke corrige y complementa la tesis de Milton Friedman y Anna Schwartz sobre la Gran Depresión.
Demuestra que la crisis de los años 30 NO fue únicamente una caída cuantitativa del stock de M1. Lo decisivo fue el COLAPSO DEL PROCESO DE INTERMEDIACIÓN FINANCIERA.
Las oleadas de quiebras bancarias destruyeron el capital de los bancos y pulverizaron las redes de información crediticia acumuladas durante décadas. Como los bancos quebrados cerraron y los supervivientes no conocían la solvencia de los deudores ajenos, el costo de intermediación crediticia se fue por las nubes. El crédito real se secó por completo, impidiendo que las empresas financiaran capital de trabajo e inversión, lo que explica por qué la Gran Depresión fue tan profunda y duró más de diez años.

• LA CRISIS FINANCIERA DE 2008 Y LA BANCA EN LA SOMBRA:
En 2022, Bernanke explica que en 2008 ocurrió una corrida bancaria análoga a la de 1929, pero no en las ventanillas de depósitos minoristas asegurados por el FDIC, sino en el 'Shadow Banking' (mercados mayoristas de deuda a corto plazo: repos y papeles comerciales respaldados por hipotecas). Al desconfiar de las hipotecas subprime, los inversores institucionales se negaron a renovar la deuda diaria a bancos de inversión (Lehman Brothers, Bear Stearns), congelando el crédito global.""",

            "t6_politica_monetaria": """• PRESTAMISTA DE ÚLTIMA INSTANCIA Y MEDIDAS NO CONVENCIONALES:
1. Doctrina de Bagehot Actualizada: Ante un pánico financiero sistémico, el Banco Central debe actuar como Prestamista de Última Instancia de forma inmediata y masiva, prestando liquidez ilimitada a entidades solventes contra buen colateral pero a tasas penalizadoras, extendiendo estas facilidades más allá de los bancos tradicionales (hacia la banca en la sombra).
2. Flexibilización Cuantitativa (Quantitative Easing - QE): Cuando las tasas de interés tocan el piso de cero (Zero Lower Bound), el banco central debe comprar masivamente activos financieros de largo plazo para comprimir las primas por plazo y restaurar el crédito hipotecario y corporativo.
3. Regulación Macroprudencial: Es indispensable complementar la política monetaria con requisitos contracíclicos de capital bancario (Basilea III), pruebas de estrés anuales obligatorias y autoridades de resolución y liquidación ordenada de instituciones financieras sistémicas (como el Título II de la Ley Dodd-Frank de 2010).""",

            "t7_expectativas_metodologia": """• MODELIZACIÓN DE EQUILIBRIO GENERAL CON FRICCIONES:
Metodológicamente, Bernanke rechaza los modelos de ciclos reales y nuevo-clásicos que asumen mercados financieros sin fricciones. Lideró la construcción de modelos macroeconómicos DSGE que incorporan microfundamentos explícitos de asimetría informacional, restricciones financieras en los balances y contratos de deuda no contingentes con riesgo de default.""",

            "t8_represion_desarrollo": """• NEXO CONCEPTUAL:
[No analiza economías en desarrollo en su conferencia Nobel de 2022].
Sin embargo, su demostración de que la destrucción de la infraestructura bancaria y el aumento del costo de intermediación estrangulan la economía real coincide plenamente con los postulados de McKinnon sobre el daño que provoca la atrofia del sistema financiero bajo represión estatal."""
        }
    },
    {
        "id": "currency_school",
        "name": "Currency School (David Ricardo, Lord Overstone, Robert Torrens)",
        "school": "Escuela Monetaria Británica Clásica del Siglo XIX",
        "epoch": "Primera mitad del Siglo XIX (1810 a 1844, culminando en la Bank Charter Act / Ley Peel)",
        "context": "Escuela que definió la arquitectura institucional bancaria de Gran Bretaña durante el siglo XIX bajo el patrón oro. Sus tesis teóricas determinaron la redacción de la Ley de Robert Peel de 1844 y sentaron las bases doctrinales para el Plan Chicago de reserva del 100% de 1933 y el movimiento moderno de Dinero Soberano (Vollgeld), analizados en el texto de Gergő Motyovszki (2016).",
        "primary_texts": ["Facu 174 (Banking School vs Currency School)", "Facu 59 (Argandoña - Definición de Dinero)"],
        "stances": {
            "t1_definicion_dinero": """• CONCEPTO ESTRICTO Y EXÓGENO DE DINERO:
Para la Currency School, el único dinero genuino es el DINERO METÁLICO (monedas y lingotes de oro) y los BILLETES DE BANCO que funcionan como certificados o sustitutos directos de dicho metal precioso.
Rechazan tajantemente considerar los depósitos bancarios en cuenta corriente, los cheques o las letras de cambio como dinero: los consideran meros instrumentos de crédito que aceleran la velocidad de circulación pero que no poseen cualidad de moneda.""",

            "t2_demanda_dinero": """• DEMANDA PASIVA TRANSACCIONAL:
Adscriben a la teoría cuantitativa clásica en su formulación más estricta. La demanda de dinero está fijada de manera pasiva e inelástica por el volumen de transacciones de mercancías físicas y el nivel de actividad económica a velocidad constante. El dinero se demanda exclusivamente para ejecutar pagos comerciales.""",

            "t3_inflacion": """• CAUSA DE LA INFLACIÓN Y DEPRECIACIÓN CAMBIARIA:
La inflación y la pérdida de valor de la libra esterlina se deben en todo momento y de forma exclusiva a la SOBREEMISIÓN DE BILLETES DE BANCO por parte de las entidades emisoras (bancos privados y el Banco de Inglaterra) sin respaldo metálico.
Cuando la cantidad de billetes en circulación excede la cantidad de oro que circularía en un régimen metálico puro, los precios internos suben, las importaciones se abaratan, la balanza comercial se vuelve deficitaria y se produce un drenaje masivo de reservas de oro hacia el exterior para pagar el déficit comercial.""",

            "t4_sistema_bancario": """• CONDENA A LA BANCA CON RESERVA FRACCIONARIA:
La Currency School formula una crítica demoledora a la capacidad de los bancos privados para emitir billetes con reserva fraccionaria. Sostienen que permitir que bancos comerciales con fines de lucro privado creen dinero a voluntad engendra una creación artificial e inestable de crédito que infla burbujas especulativas y desestabiliza a la sociedad.
Propuesta: Quitar el monopolio de emisión a los bancos privados y separar rígidamente la creación de dinero de la intermediación del crédito.""",

            "t5_crisis_fluctuaciones": """• ORIGEN DE LOS CICLOS DE AUGE Y CAÍDA (BOOM AND BUST):
Las crisis comerciales y las corridas bancarias no son eventos fortuitos ni fallas de las cosechas; son la consecuencia ineludible de la expansión crediticia desenfrenada previa:
1. Los bancos emisores expanden el crédito emitiendo billetes no respaldados a tasas bajas.
2. Esto provoca un auge artificial de precios y especulación en importaciones.
3. El déficit comercial resultante exige convertir los billetes en oro para pagar al exterior.
4. El drenaje externo de oro vacía las reservas de los bancos, forzándolos a restringir súbitamente el crédito y desatando el pánico bancario, la quiebra de comerciantes y la recesión.""",

            "t6_politica_monetaria": """• EL PRINCIPIO DE LA CIRCULACIÓN METÁLICA Y LA LEY PEEL (1844):
Prescripción institucional plasmada en la Bank Charter Act de 1844 impulsada por Robert Peel:
1. Se divide al Banco de Inglaterra en dos departamentos legalmente independientes: el Departamento de Emisión y el Departamento Bancario.
2. Se establece un cupo fiduciario fijo (£14 millones) respaldado en deuda gubernamental.
3. REGLA DEL 100%: Por encima de ese monto fiduciario, cada nuevo billete emitido debe estar respaldado en un 100% por oro físico depositado en las bóvedas del Departamento de Emisión.
4. Cero discrecionalidad: La oferta de papel moneda debe contraerse y expandirse de forma mecánica y automática exactamente al mismo ritmo que las entradas y salidas de oro por la balanza de pagos.""",

            "t7_expectativas_metodologia": """• DEDUCTIVISMO CLÁSICO RICARDIANO:
Metodología analítica basada en el razonamiento lógico-deductivo de David Ricardo, asumiendo equilibrio de largo plazo, plena flexibilidad de precios y estricta neutralidad del dinero.""",

            "t8_represion_desarrollo": """• ALCANCE HISTÓRICO:
[No aborda la represión financiera en países en desarrollo].
Su debate se circunscribió a la hegemonía financiera británica y a la estabilidad del patrón oro en el siglo XIX."""
        }
    },
    {
        "id": "banking_school",
        "name": "Banking School (Thomas Tooke, John Fullarton, James Wilson)",
        "school": "Escuela Bancaria Británica del Siglo XIX",
        "epoch": "Primera mitad del Siglo XIX (décadas de 1840 y 1850)",
        "context": "Rival teórica directa de la Currency School en el parlamento y las academias británicas. Sus aportes sobre el dinero endógeno y la elasticidad del crédito anticiparon las doctrinas de la banca central moderna, el postkeynesianismo y la teoría del circuito monetario. Obras clave: 'An Inquiry into the Currency Principle' (Thomas Tooke, 1844) y 'On the Regulation of Currencies' (John Fullarton, 1844), analizadas en el ensayo de Gergő Motyovszki (2016).",
        "primary_texts": ["Facu 174 (Banking School vs Currency School)", "Facu 59 (Argandoña - Definición de Dinero)"],
        "stances": {
            "t1_definicion_dinero": """• VISIÓN AMPLIA Y ENDÓGENA DEL DINERO:
La Banking School ataca la estrechez conceptual de la Currency School. Sostiene que es un absurdo distinguir cualitativamente entre los billetes de banco y los depósitos en cuenta corriente, los cheques o las letras de cambio comerciales.
Todos estos instrumentos cumplen idéntica función transaccional en la práctica mercantil: son medios de pago creados por la actividad financiera. La cantidad de medios de pago es ENDÓGENA y se expande o contrae en respuesta al volumen de transacciones de la economía real.""",

            "t2_demanda_dinero": """• DETERMINADA POR LAS 'NECESIDADES DEL COMERCIO' (NEEDS OF TRADE):
Para la Banking School, no es la oferta monetaria la que determina el nivel de actividad y transacciones, sino a la inversa: es la DEMANDA DE CRÉDITO Y TRANSACCIONES del sector productivo y comercial la que determina activamente la cantidad de billetes y depósitos que emite el sistema bancario. Los bancos no pueden forzar al público a retener más dinero del que necesita.""",

            "t3_inflacion": """• REFUTACIÓN DE LA TEORÍA CUANTITATIVA:
Thomas Tooke y John Fullarton demuestran que la emisión de billetes convertibles en oro NO PUEDE CAUSAR INFLACIÓN.
La causalidad cuantitativa clásica está invertida: son las variaciones en los costos de producción reales, los salarios, los precios de las materias primas y las malas cosechas las que determinan el nivel de precios de las mercancías; y este nivel de precios más alto es el que induce una mayor demanda de crédito y circulante bancario. Es el precio el que determina la cantidad de dinero, y no el dinero el que determina los precios.""",

            "t4_sistema_bancario": """• DINERO ENDÓGENO: 'LOS PRÉSTAMOS CREAN DEPÓSITOS':
Los bancos comerciales son instituciones creadoras de dinero de crédito. Cuando un comerciante solicita un descuento de letras o un préstamo, el banco no transfiere ahorros físicos previos de un tercero: crea un nuevo depósito acreditándolo en la cuenta del cliente (Loans create deposits).

• LA LEY DEL REFLUJO (LAW OF REFLUX - PIEDRA ANGULAR DE EXAMEN):
Formulada por John Fullarton: En un sistema bancario donde los billetes son legalmente convertibles en oro o donde existen deudas recíprocas, la SOBREEMISIÓN PERMANENTE DE BILLETES ES IMPOSIBLE.
Mecanismo: Si un banco intenta emitir más billetes de los que el público requiere para sus transacciones cotidianas, ese exceso de papel moneda no permanece circulando ni infla los precios de los bienes; REFLUYE inmediatamente hacia los bancos emisores a través de tres canales:
1. Cancelación de préstamos bancarios vencidos.
2. Constitución de nuevos depósitos bancarios que rinden interés.
3. Presentación al banco para su conversión en oro si el público desea atesorar metal.

• LA DOCTRINA DE LAS LETRAS REALES (REAL BILLS DOCTRINE):
Si los bancos conceden crédito respaldado exclusivamente en letras comerciales genuinas de corto plazo (a 60 o 90 días) emitidas para financiar la producción o transporte de bienes reales en movimiento hacia el mercado, la oferta monetaria se auto-regulará con perfecta elasticidad según el ciclo productivo y nunca generará inflación.""",

            "t5_crisis_fluctuaciones": """• ORIGEN REAL DE LAS CRISIS Y CRÍTICA A LA LEY PEEL:
Las crisis comerciales se originan en perturbaciones reales: sobreespeculación en cosechas o materias primas, guerras o caídas de confianza de los negocios.
La advertencia profética de la Banking School: Imponer un tope rígido de emisión respaldado 100% en oro (como hizo la Ley Peel de 1844) es un error fatal. Cuando estalla un pánico comercial, la demanda de liquidez se dispara; si la ley prohíbe a los bancos emitir billetes porque se drenó oro temporalmente, se estrangula la liquidez del mercado, forzando a comerciantes y bancos perfectamente solventes a la suspensión de pagos y transformando una corrección normal en una catástrofe financiera generalizada (como ocurrió en 1847, 1857 y 1866, donde el gobierno británico tuvo que suspender de emergencia la Ley Peel para permitir que el Banco de Inglaterra emitiera sin respaldo y frenara el pánico).""",

            "t6_politica_monetaria": """• OFERTA MONETARIA ELÁSTICA:
La autoridad monetaria debe proveer una oferta monetaria elástica que acompañe el ciclo de negocios y actúe con flexibilidad en momentos de estrés.
El Banco de Inglaterra debe mantener reservas metálicas holgadas no para fijar una camisa de fuerza a los billetes, sino para absorber salidas transitorias de oro sin necesidad de contraer violentamente el crédito al comercio legítimo.""",

            "t7_expectativas_metodologia": """• EMPIRISMO INDUCTIVO E HISTÓRICO:
Thomas Tooke desarrolló su monumental 'History of Prices' (6 volúmenes), reuniendo datos empíricos de precios durante más de un siglo para refutar con evidencia estadística las deducciones simplistas de David Ricardo y la Currency School.""",

            "t8_represion_desarrollo": """• CONEXIÓN:
[No aborda economías subdesarrolladas contemporáneas].
Su principio de que el crédito debe acompañar las necesidades del comercio y no ser racionado burocráticamente es coherente con las críticas a la represión bancaria."""
        }
    },
    {
        "id": "mckinnon",
        "name": "Ronald I. McKinnon (& Edward S. Shaw)",
        "school": "Economía del Desarrollo Financiero (Hipótesis McKinnon-Shaw)",
        "epoch": "Década de 1970 (1973 – 1978)",
        "context": "Profesor de la Universidad de Stanford y pionero indiscutido del estudio de la intermediación bancaria en países en vías de desarrollo (LDCs). Su libro seminal 'Money and Capital in Economic Development' (1973) y su ensayo 'Represión financiera y el problema de la liberalización dentro de los países menos desarrollados' (1978) transformaron las políticas económicas en América Latina y Asia, demostrando cómo la intervención estatal asfixia el crecimiento económico.",
        "primary_texts": ["Facu 66 (Represión Financiera y el Problema de la Liberalización)"],
        "stances": {
            "t1_definicion_dinero": """• FOCO EN M2 COMO ACTIVO DE AHORRO POPULAR:
McKinnon analiza el dinero desde la estructura real de los países atrasados: dado que los mercados de bonos abiertos, acciones y títulos hipotecarios son minúsculos o inexistentes, el dinero y los depósitos bancarios a plazo (M2 = Circulante + Depósitos en bancos comerciales) representan la casi totalidad de los activos financieros acumulables por las familias y pequeñas empresas.""",

            "t2_demanda_dinero": """• DEMANDA DE SALDOS REALES BAJO REPRESIÓN:
Formula una función de demanda de saldos monetarios reales adaptada al subdesarrollo:
(M / P)^d = f(Y, r - π^e, I/Y)
Donde (r - π^e) es la TASA DE INTERÉS REAL de los depósitos bancarios.
Demuestra empíricamente que en países en desarrollo, si el gobierno mantiene tasas nominales congeladas en presencia de alta inflación, la tasa real de rendimiento de los depósitos se vuelve fuertemente negativa. Ante esto, la demanda de saldos reales se desploma, el público huye del sistema bancario formal y el ratio de monetización M2/PBI colapsa a niveles raquíticos (0.15 o 0.20 en países reprimidos frente a 0.60 a 0.75 en economías desarrolladas).""",

            "t3_inflacion": """• LA INFLACIÓN COMO INSTRUMENTO EXPROPIATORIO:
La inflación crónica en el Tercer Mundo no es un accidente, sino una técnica coercitiva deliberada del Estado para extraer un 'excedente económico' mediante el IMPUESTO INFLACIONARIO para subsidiar la industrialización sustitutiva urbana.
Este impuesto erosiona el valor del dinero, castiga al pequeño ahorrista rural y destruye el mercado formal de crédito.""",

            "t4_sistema_bancario": """• EL SISTEMA BANCARIO REPRIMIDO:
Bajo la 'represión financiera', el sector bancario doméstico es sometido a un laberinto de controles:
1. Techos legales a las tasas pasivas (que desincentivan el ahorro) y a las tasas activas (que generan exceso de demanda de crédito).
2. Encajes bancarios confiscatorios (a menudo del 40% al 80%), no remunerados, utilizados por el gobierno como crédito fiscal encubierto.
3. Racionamiento burocrático y discrecional del crédito: Al haber tasas subsidiadas negativas, los bancos no asignan fondos por rentabilidad o solvencia, sino hacia prestatarios políticamente favorecidos (grandes empresas estatales o conglomerados industriales urbanos).
4. El resto de la economía (especialmente el sector agropecuario y las pequeñas empresas industriales) queda marginado por completo del crédito formal.""",

            "t5_crisis_fluctuaciones": """• LA TRAMPA DEL SUBDESARROLLO Y EL AUTOFINANCIAMIENTO ARCAICO:
La fragilidad económica crónica de los países pobres no responde a insuficiencia de demanda keynesiana, sino a la FRAGMENTACIÓN FINANCIERA:
Al no haber crédito bancario disponible para los pequeños productores, estos se ven forzados al AUTOFINANCIAMIENTO estricto a partir de sus propios ahorros retenidos.
Como este ahorro retenido es ilíquido y de pequeña escala, los agricultores y pequeños empresarios quedan atrapados utilizando tecnologías obsoletas e ineficientes, perpetuando la baja productividad y el subdesarrollo.""",

            "t6_politica_monetaria": """• REFORMA DEL BANCO CENTRAL:
El Banco Central debe abandonar el rol de agencia de financiamiento espurio del tesoro y prestamista de créditos dirigidos subsidiados.
Debe reducir drásticamente los encajes legales para liberar fondos prestables al sector privado y concentrarse en erradicar la inflación que destruye el sistema de precios del crédito.""",

            "t7_expectativas_metodologia": """• ANÁLISIS MICROECONÓMICO INSTITUCIONAL:
Metodológicamente, McKinnon modela los incentivos de carteras de inversión y ahorro bajo restricciones severas de mercado e indivisibilidades tecnológicas en economías emergentes.""",

            "t8_represion_desarrollo": """• LA HIPÓTESIS DE COMPLEMENTARIEDAD ENTRE DINERO Y CAPITAL (EJE DE EXAMEN):
Es la contribución teórica más famosa de McKinnon, que choca frontalmente con la teoría neoclásica tradicional (Tobin):
- En la teoría neoclásica de carteras (Tobin): El dinero y el capital físico son ACTIVOS COMPETIDORES o sustitutos (si la rentabilidad del dinero sube, los agentes retienen más dinero y compran menos capital físico).
- En la teoría de McKinnon para países en desarrollo: El dinero y la inversión en capital físico son COMPLEMENTARIOS.
Por qué: Dado que los bienes de capital productivo (un tractor, un telar, un generador) son altamente costosos e INDIVISIBLES, y dado que en los países en desarrollo no existen mercados abiertos de crédito de largo plazo para la pequeña empresa o el agricultor, el inversor debe AHORRAR PREVIAMENTE SALDOS MONETARIOS REALES durante meses o años para poder comprar la máquina al contado.
Por ende, para que haya inversión en capital físico, debe haber primero acumulación de saldos monetarios en M2.
Si el gobierno reprime el sistema financiero pagando tasas reales de interés fuertemente negativas (r - π < 0), el valor de los ahorros monetarios se evapora mes a mes, la acumulación previa se vuelve imposible y la inversión física se DERRUMBA.

• LA RECETA DE LIBERALIZACIÓN FINANCIERA:
Para salir del subdesarrollo, el gobierno debe:
1. Liberar las tasas de interés para que sean POSITIVAS EN TÉRMINOS REALES (r > π), remunerando adecuadamente al ahorrista y reflejando la verdadera escasez del capital.
2. Unificar los mercados de crédito y reducir los encajes bancarios.
3. Esto disparará la intermediación financiera (profundización financiera, financial deepening), elevará el ratio M2/PBI y permitirá que los fondos fluyan desde el consumo suntuario hacia las inversiones más productivas de la economía."""
        }
    },
    {
        "id": "olivera_canavese",
        "name": "Julio H. G. Olivera y Alfredo Canavese",
        "school": "Estructuralismo Latinoamericano / Escuela Estructuralista de la Inflación",
        "epoch": "Décadas de 1950 a 1980 (CEPAL, UBA / Ensayo clásico de Canavese 1979 republicado en 2009)",
        "context": "Máximos exponentes de la formalización matemática del estructuralismo latinoamericano. Julio H. G. Olivera (Universidad de Buenos Aires) formuló la teoría del 'dinero pasivo' en 1957/1960, y Alfredo Canavese (1979) demostró la equivalencia formal matemática entre la inflación estructural cepalina y los modelos de traslación de demanda anglosajones (Schultze, Baumol). Su trabajo es el núcleo de 'La hipótesis estructural en la teoría de la inflación' (Facu 72).",
        "primary_texts": ["Facu 72 (La Hipótesis Estructural en la Teoría de la Inflación - Ensayos BCRA 2009)"],
        "stances": {
            "t1_definicion_dinero": """• DINERO PASIVO Y CONVALIDANTE:
Rechazan la noción de que la masa monetaria sea una variable autónoma o exógena manipulada a discreción por el Banco Central.
El dinero es concebido como una variable ENDÓGENA Y PASIVA: un medio de pago cuya cantidad en circulación se expande para convalidar las presiones de precios relativos generadas en la estructura productiva real.""",

            "t2_demanda_dinero": """• DEMANDA CONDICIONADA POR EL COSTO DE PRODUCCIÓN:
La demanda agregada de saldos monetarios responde a la necesidad ineludible del sistema productivo de disponer de medios de pago suficientes para mantener el nivel de transacciones, empleo y actividad económica frente al encarecimiento de los costos de producción y bienes salario provocado por los estrangulamientos sectoriales.""",

            "t3_inflacion": """• LA TEORÍA ESTRUCTURALISTA DE LA INFLACIÓN (EJE CENTRAL DE EXAMEN):
La causa originaria del alza de precios NO es monetaria ni proviene de un exceso de demanda agregada global. La inflación surge de la interacción necesaria de tres elementos inseparables:

1. Estrangulamientos Sectoriales y Cambios en la Estructura Económica: En el proceso de desarrollo y crecimiento urbano, se producen cuellos de botella por rigideces de oferta:
   - Estrangulamiento Agrícola: La producción de alimentos es inelástica (debido al régimen de tenencia de la tierra y falta de inversión); el aumento de la demanda urbana presiona fuertemente sobre el precio de los alimentos.
   - Estrangulamiento Externo: Escasez estructural de divisas por deterioro de los términos de intercambio (Prebisch-Singer), forzando devaluaciones periódicas que encarecen insumos importados.
   - Estos estrangulamientos exigen un CAMBIO INELUDIBLE EN LOS PRECIOS RELATIVOS a favor de los sectores con oferta rígida.
2. Inflexibilidad a la Baja de Precios Monetarios y Salarios: En los sectores dinámicos o con exceso de oferta, los precios nominales y salarios son RÍGIDOS A LA BAJA (no disminuyen por fijación de márgenes monopólicos y defensa del salario monetario).
3. Consecuencia: Dado que los precios relativos deben cambiar necesariamente, y como los precios de los sectores estrangulados suben pero los de los demás sectores no pueden bajar, el único modo de ajustar la relación de precios es elevando el NIVEL GENERAL DE PRECIOS de toda la economía.

• LA EQUIVALENCIA FORMAL DEMOSTRADA POR ALFREDO CANAVESE (1979):
Canavese prueba formalmente con rigor matemático que el modelo de inflación estructural latinoamericano (Noyola, Sunkel, Olivera) es formalmente equivalente al modelo de traslación de demanda de Charles Schultze (1959 en EE.UU., demand-shift inflation) y al modelo de inflación de productividad de William Baumol (1967) y el modelo escandinavo de Aukrust.""",

            "t4_sistema_bancario": """• EL TEOREMA DE LA OFERTA MONETARIA PASIVA DE JULIO H. G. OLIVERA (1957/1960):
Punto nodal para examen: ¿Por qué la cantidad de dinero acompaña a los precios si la causa no es monetaria?
Olivera formula el teorema del Dinero Pasivo:
1. El shock de precios relativos e inflexibilidad a la baja eleva el nivel general de precios (P sube).
2. Si el Banco Central mantuviera la cantidad de dinero (M) fija y congelada, los saldos monetarios reales (M/P) se contraerían bruscamente.
3. Esta contracción de liquidez abriría una 'BRECHA DEFLACIONARIA': provocaría iliquidez generalizada, acumulación de inventarios invendibles, quiebras masivas de empresas solventes y desempleo masivo.
4. Para evitar la parálisis del aparato productivo y el colapso social, la autoridad monetaria se ve obligada institucionalmente a emitir dinero de forma pasiva, convalidando el nivel de precios más alto.
Por tanto, la emisión monetaria es la CONSECUENCIA, no la causa, del proceso inflacionario.""",

            "t5_crisis_fluctuaciones": """• RECESIONES INDUCIDAS POR PLANES DE SHOCK ORTODOXOS:
Las crisis recesivas agudas en América Latina son frecuentemente generadas por la aplicación ciega de programas de estabilización monetaristas ortodoxos (recetas del FMI).
Al intentar cortar la inflación contrayendo bruscamente el crédito y la oferta monetaria en economías que sufren estrangulamientos reales, las autoridades no resuelven la inelasticidad agraria ni la falta de divisas, pero logran quebrar al sector productivo, desplomando el PBI y generando estanflación severa.""",

            "t6_politica_monetaria": """• LÍMITES DE LA POLÍTICA MONETARIA Y POLÍTICAS DE DESARROLLO:
La política monetaria contractiva convencional es estéril contra la inflación estructural: solo puede frenar los precios al costo de sumir al país en una depresión catastrófica.
Prescripción: La única solución duradera es la POLÍTICA ESTRUCTURAL Y DE DESARROLLO:
1. Eliminar los cuellos de botella reales: reforma agraria y tecnificación para elevar la elasticidad de oferta de alimentos.
2. Diversificación exportadora e industrialización para superar la restricción externa de divisas.
3. Inversión pública en infraestructura energética y logística.""",

            "t7_expectativas_metodologia": """• METODOLOGÍA ESTRUCTURALISTA:
Rechazo de los modelos abstractos de equilibrio general que asumen mercados perfectos, homogéneos y sin fricciones. La economía real se caracteriza por heterogeneidad estructural, oligopolios, asimetrías de poder y mercados segmentados.""",

            "t8_represion_desarrollo": """• EL ESTRANGULAMIENTO EXTERNO COMO RESTRICCIÓN REAL:
Para los estructuralistas, las restricciones financieras y cambiarias en América Latina no son simples fallas de política que se resuelven liberando las tasas de interés como propone McKinnon, sino la consecuencia del estrangulamiento externo de la balanza de pagos originado en la división internacional del trabajo."""
        }
    },
    {
        "id": "werning_lorenzoni",
        "name": "Guido Lorenzoni e Iván Werning",
        "school": "Macroeconomía Contemporánea / Escuela del Conflicto Distributivo",
        "epoch": "2022 – 2023 (Macroeconomía Post-Pandemia, MIT / Northwestern University)",
        "context": "Destacados teóricos de la macroeconomía moderna en el MIT y Northwestern University. En su trabajo 'Inflation is Conflict' (NBER, abril de 2023), desentrañan las raíces microfundamentadas de la inflación tras el repunte inflacionario global post-COVID-19, rescatando y formalizando la teoría postkeynesiana del conflicto distributivo en un marco analítico contemporáneo.",
        "primary_texts": ["Facu 179 (Inflation is Conflict)"],
        "stances": {
            "t1_definicion_dinero": """• EL DINERO COMO ELEMENTO PRESCINDIBLE PARA LA INFLACIÓN:
Aporte epistemológico provocador: Lorenzoni y Werning demuestran matemáticamente que el dinero físico es totalmente secundario e innecesario para que exista y persista la inflación.
En la primera parte de su trabajo presentan un modelo estilizado donde NO EXISTE dinero, crédito, tasas de interés, producción ni empleo, y aun así la inflación florece y se sostiene en el tiempo.""",

            "t2_demanda_dinero": """• AISLAMIENTO ANALÍTICO:
[No abordan la demanda convencional de dinero].
Suprimieron deliberadamente el mercado monetario de su modelo para aislar con absoluta pureza el mecanismo del conflicto distributivo sobre los precios.""",

            "t3_inflacion": """• LA TESIS CENTRAL: 'LA INFLACIÓN ES CONFLICTO':
La inflación es en su esencia la manifestación visible del CONFLICTO O DESACUERDO DISTRIBUTIVO entre los agentes económicos por la apropiación del ingreso nacional disponible.
Surge porque las pretensiones de participación de los distintos sectores son MUTUAMENTE INCOMPATIBLES:
La suma del salario real deseado por los trabajadores (w/p)^d y el margen de beneficio o markup deseado por las empresas (P/W)^d supera el 100% de la torta productiva disponible.

• EL MECANISMO DE ESCALONAMIENTO TEMPORAL Y LA ESPIRAL SALARIOS-PRECIOS:
Dado que los agentes no pueden renegociar precios y salarios continuamente al unísono, se produce una fijación escalonada y asincrónica en el tiempo (tipo contratos de Calvo):
1. Los trabajadores perciben que su salario real cayó y aumentan sus salarios nominales en su turno de negociación.
2. Al aumentar los costos laborales, las firmas suben inmediatamente los precios de sus bienes para defender su margen de beneficio deseado.
3. La suba de precios erosiona de nuevo el salario real de los trabajadores.
4. En el siguiente turno, los trabajadores vuelven a demandar aumentos salariales nominales.
5. Resultado: Una ESPIRAL SALARIOS-PRECIOS (wage-price spiral). El conflicto por modificar los precios relativos termina en un empate frustrado para ambos en términos reales, pero como subproducto engendra una tasa sostenida y positiva de inflación en todos los precios nominales.

• DESCOMPOSICIÓN ANALÍTICA: INFLACIÓN DE AJUSTE VS INFLACIÓN DE CONFLICTO (CLAVE PARA EXAMEN):
Lorenzoni y Werning descomponen la inflación observada en dos componentes analíticos:
1. Inflación de Ajuste (Adjustment Inflation): Es el cambio de precios transitorio derivado del reacomodamiento eficiente de precios relativos tras un shock real; es acotada en magnitud, de corta duración y se extingue sola.
2. Inflación de Conflicto (Conflict Inflation): Es la inflación persistente y duradera alimentada por la lucha distributiva entre márgenes y salarios reales. Es la causa próxima fundamental de la persistencia inflacionaria.""",

            "t4_sistema_bancario": """• ROL SECUNDARIO DEL CRÉDITO:
[No es el eje del artículo].
El sistema crediticio puede lubricar y facilitar los medios de pago para que las transacciones se liquiden a precios más altos, pero la fuerza motriz originaria reside en la puja distributiva de la economía real.""",

            "t5_crisis_fluctuaciones": """• SHOCKS DE OFERTA Y AGUDIZACIÓN DEL CONFLICTO:
Las aceleraciones inflacionarias se desencadenan cuando shocks reales negativos (shocks en el precio de la energía, deterioro de términos de intercambio, caída de productividad post-pandemia) REDUCEN EL TAMAÑO DE LA TORTA PRODUCTIVA DISPONIBLE.
Al haber menos producto real para repartir, las aspiraciones previas de salarios y beneficios chocan con mayor violencia, intensificando la espiral salarios-precios.""",

            "t6_politica_monetaria": """• EL VERDADERO CANAL DE TRANSMISIÓN DE LA SUBA DE TASAS:
Reinterpretan cómo opera la política monetaria de los bancos centrales:
Subir la tasa de interés no frena la inflación por un acto de magia cuantitativa sobre los billetes.
La política monetaria contractiva reduce la inflación porque ENFRÍA LA DEMANDA AGREGADA Y ELEVA EL DESEMPLEO:
Al deprimir las ventas, debilita el poder de fijación de márgenes de las empresas; y al aumentar el desempleo, debilita el poder de negociación de los sindicatos y trabajadores.
En términos crudos: la política monetaria fuerza un 'armisticio obligatorio' en el conflicto distributivo, obligando a las partes a tolerar una menor tajada de la torta para frenar la espiral.""",

            "t7_expectativas_metodologia": """• PUENTE DOCTRINAL:
Metodológicamente, construyen un puente matemático riguroso que une la tradición postkeynesiana del conflicto social (Robert Rowthorn, 1977; Marc Lavoie) con los modelos Nuevo Keynesianos microfundamentados con rigideces nominales de precios y salarios.""",

            "t8_represion_desarrollo": """• ALCANCE ANALÍTICO:
[No aborda la represión financiera en países en desarrollo].
Su marco se orienta a la teoría general de la inflación contemporánea en economías de mercado abiertas."""
        }
    },
    {
        "id": "shackle_earl",
        "name": "George L. S. Shackle (y Peter E. Earl)",
        "school": "Postkeynesianismo Conductual / Teoría de la Incertidumbre Radical",
        "epoch": "Mediados y finales del Siglo XX (1940s a 1980s, rescatado por Earl en 2018)",
        "context": "Economista británico (1903–1992), discípulo simultáneo de Keynes en Cambridge y Hayek en LSE. Formuló la crítica más radical y profunda a la teoría de la elección neoclásica y al cálculo probabilístico en economía. El texto analizado es 'G. L. S. Shackle’s introspective behavioral economics' de Peter E. Earl (Journal of Behavioral Economics for Policy, 2018).",
        "primary_texts": ["Facu 86 (G. L. S. Shackle’s introspective behavioral economics)"],
        "stances": {
            "t1_definicion_dinero": """• EL DINERO COMO ESCUDO PSICOLÓGICO FRENTE A LO DESCONOCIDO:
Para Shackle, el dinero es el activo supremo que otorga 'inmunidad contra el compromiso en un mundo incierto'.
Su naturaleza no se agota en ser un lubricante transaccional: es la posesión de un activo que preserva abiertas todas las opciones futuras frente a un destino que no puede calcularse.""",

            "t2_demanda_dinero": """• FUNDAMENTO INTROSPECTIVO DE LA PREFERENCIA POR LA LIQUIDEZ:
Brinda la justificación psicológica última de la demanda de dinero keynesiana. Los individuos no demandan dinero por resolver un problema rutinario de inventarios o varianzas numéricas, sino porque enfrentan una angustia real ante la ignorancia del futuro. Demandar liquidez es la respuesta instintiva para no atar los recursos a compromisos de capital fijos e irrevocables.""",

            "t3_inflacion": """• ENFOQUE NO MONETARISTA:
[No formula una teoría sistemática de la inflación].
Su obra se concentró en la epistemología de la elección, el tiempo humano y la formación de expectativas en la inversión empresarial.""",

            "t4_sistema_bancario": """• APUESTAS EN UN TIEMPO HISTÓRICO IRREVERSIBLE:
Los bancos operan en un entorno de incertidumbre radical donde cada contrato de préstamo es una apuesta sobre proyectos futuros que aún no existen y cuyos resultados no pueden computarse con distribuciones de probabilidad objetivas.""",

            "t5_crisis_fluctuaciones": """• EL COLAPSO DE LOS ESCENARIOS IMAGINADOS Y LA SORPRESA:
Las crisis económicas ocurren cuando se desmoronan los escenarios mentales de los inversores:
1. En períodos de calma, los empresarios operan basándose en convenciones frágiles y visiones optimistas imaginadas.
2. Cuando ocurre un hecho imprevisto de alta 'sorpresa potencial', las convenciones colapsan instantáneamente en pánico.
3. La parálisis mental destruye la voluntad de invertir, disparando la preferencia por la liquidez y sumiendo a la economía en recesión.""",

            "t6_politica_monetaria": """• ESCEPTICISMO FRENTE A LA TECNOCRACIA DE BANCOS CENTRALES:
Shackle es sumamente escéptico ante la pretensión de que los bancos centrales puedan dirigir mecánicamente la economía con modelos econométricos: los agentes reaccionan ante las medidas con imaginación subjetiva, cambiando impredeciblemente sus decisiones.""",

            "t7_expectativas_metodologia": """• INCERTIDUMBRE RADICAL VERSUS RIESGO (EJE CENTRAL DE EXAMEN):
Crítica demoledora a la Teoría de la Utilidad Esperada y a las Expectativas Racionales:
1. Riesgo vs Incertidumbre: El riesgo se aplica a eventos repetibles con distribuciones de frecuencia conocidas (ruleta, seguros actuariales). Las decisiones económicas de inversión son experimentos ÚNICOS e IRREPETIBLES en un tiempo histórico irreversible. Como el futuro aún no ha sido creado, NO existen distribuciones de probabilidad esperando ser descubiertas.
2. El 'Momento del Presente' (Moment-in-Being): La elección solo existe en el instante presente ex-ante basada en la imaginación humana creadora. El resultado ex-post es historia inmutable.
3. Teoría de la Sorpresa Potencial y Focos de Decisión:
   - Los individuos asignan a cada hipótesis un grado de sorpresa potencial (y), desde cero para lo creíble hasta sorpresa máxima para lo inverosímil.
   - Focos de Ganancia y Pérdida (Focus outcomes): La atención del inversor se polariza en el mejor resultado concebible y en la peor pérdida concebible que no generarían sorpresa. La decisión se toma ponderando estos dos puntos focales.
4. Precursor de la racionalidad acotada de Herbert Simon y la Teoría de las Perspectivas de Kahneman y Tversky.""",

            "t8_represion_desarrollo": """• ALCANCE DOCTRINAL:
[No aborda economías en desarrollo en este texto].
Focalizado en la teoría epistemológica de la decisión bajo incertidumbre."""
        }
    },
    {
        "id": "zuleta_cagan",
        "name": "Hernando Zuleta G. (y Philip Cagan)",
        "school": "Finanzas Públicas Monetarias / Enfoque del Impuesto Inflacionario",
        "epoch": "1956 (Cagan) / 1995 (Zuleta, Borradores Semanales de Economía, Banco de la República)",
        "context": "Hernando Zuleta G. analiza la restricción presupuestaria del gobierno y los límites matemáticos del financiamiento monetario del gasto público en el Banco de la República de Colombia (1995), aplicando el modelo clásico de hiperinflaciones de Philip Cagan (1956) en 'Impuesto Inflacionario y Señoreaje' (Facu 95).",
        "primary_texts": ["Facu 95 (Impuesto Inflacionario y Señoreaje)", "Facu 97 (Demanda de Dinero)"],
        "stances": {
            "t1_definicion_dinero": """• LA BASE MONETARIA COMO BASE IMPONIBLE:
Se concentra en la Base Monetaria (B = Efectivo en manos del público + Reservas bancarias legales inmovilizadas en el Banco Central), ya que representa la base imponible sobre la cual el Estado ejerce su monopolio legal de emisión para extraer recursos de la economía.""",

            "t2_demanda_dinero": """• LA DEMANDA DE DINERO DE PHILIP CAGAN (1956):
Adopta la función semilogarítmica de demanda de saldos monetarios reales para contextos inflacionarios:
m = A · e^(-α · π^e)
Donde m = M/P (saldos reales), π^e es la tasa esperada de inflación y α es la semielasticidad de la demanda de dinero respecto a la inflación.
A medida que la inflación esperada sube, el público reduce exponencialmente la tenencia de saldos reales para escapar del impuesto inflacionario.""",

            "t3_inflacion": """• LA INFLACIÓN COMO MECANISMO TRIBUTARIO FISCAL:
La causa primaria de la inflación es el financiamiento monetario inorgánico de un DÉFICIT FISCAL estructural cuando el Estado no tiene acceso a financiamiento mediante deuda genuina ni puede elevar impuestos tributarios ordinarios.""",

            "t4_sistema_bancario": """• MANIPULACIÓN DE LOS ENCAJES BANCARIOS:
Los encajes bancarios obligatorios impuestos a los bancos comerciales son analizados como una herramienta fiscal coercitiva:
Al obligar a los bancos a mantener reservas no remuneradas en el Banco Central, el gobierno agranda la base cautiva del impuesto inflacionario, recaudando más recursos a corto plazo a expensas de encarecer el crédito productivo.""",

            "t5_crisis_fluctuaciones": """• LA DINÁMICA DE LA HIPERINFLACIÓN EXPLOSIVA:
Las crisis hiperinflacionarias estallan cuando el gobierno intenta recaudar una cantidad de señoreaje mayor que el máximo de la curva de Laffer (SE > A / (α · e)).
La aceleración de la emisión provoca una caída tan colosal de la demanda de saldos reales que la recaudación disminuye, forzando a emitir aún más rápido en una espiral que destruye la moneda.""",

            "t6_politica_monetaria": """• DOMINANCIA FISCAL (FISCAL DOMINANCE):
La política monetaria está totalmente subordinada a las necesidades de financiamiento del tesoro público.
Para eliminar la inflación es indispensable eliminar el déficit presupuestario y consagrar la prohibición legal de que el Banco Central financie al gobierno.""",

            "t7_expectativas_metodologia": """• FORMALIZACIÓN MATEMÁTICA Y ESTADO ESTACIONARIO:
Diferenciación analítica fundamental (EJE DE EXAMEN):
1. Impuesto Inflacionario (TI): Pérdida de capital real que sufren los tenedores de saldos monetarios por la pérdida de poder adquisitivo del dinero:
   TI_t = (P_dot / P) · (M / P) = π · m
2. Señoreaje (SE): Recursos reales brutos percibidos por el gobierno por la emisión de base monetaria:
   SE_t = M_dot / P
3. Relación Dinámica:
   Derivando los saldos reales m = M/P con respecto al tiempo:
   m_dot = (M_dot / P) - π · m = SE - TI  ===>  SE = m_dot + TI
4. En ESTADO ESTACIONARIO (m_dot = 0):
   El señoreaje coincide exactamente con el impuesto inflacionario (SE = TI).

• CURVA DE LAFFER DEL SEÑOREAJE:
Recaudación: TI(π) = π · A · e^(-α · π)
Derivando con respecto a π e igualando a cero:
dTI/dπ = A · e^(-απ) · (1 - α · π) = 0  ===>  π* = 1 / α
La tasa de inflación que maximiza los ingresos del gobierno es exactamente la inversa de la semielasticidad de la demanda de dinero (1/α). Emitir por encima de esa tasa genera caída de la recaudación real.""",

            "t8_represion_desarrollo": """• LÓGICA DE LA REPRESIÓN FINANCIERA:
Explica con claridad por qué los países en desarrollo recurren a la represión financiera: al elevar los encajes y congelar las tasas, el gobierno crea cautiverio financiero para extraer señoreaje del sistema bancario."""
        }
    },
    {
        "id": "harry_johnson",
        "name": "Harry G. Johnson",
        "school": "Historia del Pensamiento / Universidad de Chicago y LSE",
        "epoch": "1971 (Cúspide de la controversia Keynesianismo vs Monetarismo)",
        "context": "Destacado macroeconomista internacional de la Universidad de Chicago y la London School of Economics. Su célebre ensayo 'Revolución y contrarrevolución en economía' (1971, Facu 64) analiza con lucidez sociológica e histórica cómo nacen, triunfan y decaen las corrientes teóricas en la profesión económica.",
        "primary_texts": ["Facu 64 (Revolución y contrarrevolución en economía)"],
        "stances": {
            "t1_definicion_dinero": """• EL CONCEPTO DE DINERO COMO BANDERA DOCTRINAL:
Analiza la definición de dinero desde la sociología académica: el debate entre M1 y M2 no fue una simple discusión estadística, sino el campo de batalla donde el monetarismo de Friedman desafió a la ortodoxia keynesiana para demostrar empíricamente que 'el dinero importa'.""",

            "t2_demanda_dinero": """• LA MANIOBRA TÁCTICA DE MILTON FRIEDMAN:
Johnson desentraña la estrategia de Friedman: en lugar de resucitar la teoría cuantitativa clásica rígida (que asumía V constante y era fácilmente refutable por los keynesianos), Friedman reformuló la teoría cuantitativa como una función de demanda de dinero ESTABLE, adoptando el lenguaje formal de Keynes para invertir sus conclusiones de política.""",

            "t3_inflacion": """• LA FALLA KEYNESIANA FRENTE A LA INFLACIÓN:
La incapacidad de la síntesis keynesiana para explicar y frenar la inflación en economías de posguerra con pleno empleo fue la vulnerabilidad empírica que permitió el triunfo social de la contrarrevolución monetarista de Chicago.""",

            "t4_sistema_bancario": """• METATEORÍA DE LA TRANSMISIÓN:
[Tratamiento sociológico e institucional].
Analiza cómo la profesión económica pasó de ignorar a los bancos bajo el fiscalismo keynesiano vulgar a colocarlos en el centro de la escena con el monetarismo.""",

            "t5_crisis_fluctuaciones": """• LAS CONDICIONES PARA UNA REVOLUCIÓN ECONÓMICA (EJE DE EXAMEN):
Una teoría económica solo triunfa si responde a una crisis empírica real que la ortodoxia previa no puede resolver:
- El desempleo masivo de la Gran Depresión creó a la Revolución Keynesiana.
- La inflación de posguerra creó a la Contrarrevolución Monetarista.""",

            "t6_politica_monetaria": """• LAS REGLAS MONETARIAS COMO ATRACTIVO POLÍTICO:
Las propuestas monetaristas de reglas fijas (k%) tuvieron éxito no solo por su coherencia teórica, sino porque ofrecían un producto intelectual seductor para los sectores políticos conservadores que buscaban limitar el gasto público y el intervencionismo estatal.""",

            "t7_expectativas_metodologia": """• SOCIOLOGÍA DEL CONOCIMIENTO ACADÉMICO (LOS 5 REQUISITOS):
1. Atacar una ortodoxia que fracasó en los hechos.
2. Apariencia de realismo e intuición atractiva.
3. Metodología nueva y difícil que entusiasme a investigadores jóvenes y margine a los profesores viejos.
4. Recetas aplicables para los gobiernos.
5. Un programa fértil de investigación empírica.
Profecía de Johnson: El monetarismo decaerá cuando se vuelva dogma y la innovación financiera vuelva inestables a los agregados monetarios.""",

            "t8_represion_desarrollo": """• ALCANCE DOCTRINAL:
[No aborda la represión financiera en este texto].
Centrado en la política universitaria y académica anglosajona."""
        }
    },
    {
        "id": "clasicos_poskeynesianos",
        "name": "Clásicos y Poskeynesianos (Fisher, Pigou, Baumol, Tobin)",
        "school": "Tradición Cuantitativa Clásica / Escuela de Cambridge / Síntesis Neoclásica",
        "epoch": "Finales del Siglo XIX a Década de 1950",
        "context": "Constructores de los cimientos analíticos y microeconómicos de la teoría de la demanda de dinero analizados exhaustivamente en el trabajo de Álvaro Chaves Barea (Facu 97): Irving Fisher (1911), Alfred Marshall y Arthur C. Pigou (1917, 1923), William Baumol (1952) y James Tobin (1956, 1958).",
        "primary_texts": ["Facu 97 (Demanda de Dinero - Chaves Barea)", "Facu 59 (Argandoña - Definición de Dinero)"],
        "stances": {
            "t1_definicion_dinero": """• EVOLUCIÓN CONCEPTUAL:
- Fisher: Medio de pago puro para transacciones inmediatas (circulante físico).
- Marshall y Pigou: Medio de cambio y reserva de valor individual (saldos de caja).
- Baumol y Tobin: Activo con costo de transacción cero pero con costo de oportunidad en tasa de interés frente a bonos.""",

            "t2_demanda_dinero": """• LAS 4 GRANDES ETAPAS ANALÍTICAS (CLAVE DE EXAMEN):

1. Irving Fisher (1911) – Teoría Cuantitativa de Transacciones:
   Ecuación de Intercambio: M · V = P · T
   El dinero se demanda exclusivamente para ejecutar transacciones comerciales. V (velocidad) y T (transacciones) están fijos a corto plazo por hábitos institucionales y pleno empleo. El dinero es un velo neutral.

2. Escuela de Cambridge (Marshall y Pigou, 1917/1923) – Saldos de Caja:
   Ecuación de Cambridge: M^d = k · P · Y
   Introduce la decisión individual de atesoramiento. Los agentes desean mantener una proporción k (k = 1/V) de su ingreso nominal en saldos monetarios por seguridad y conveniencia (reserva de valor).

3. William Baumol (1952) y James Tobin (1956) – Modelo de Inventarios para Transacciones:
   Microfundamentación matemática: el motivo transacción keynesiano TAMBIÉN depende negativamente de la tasa de interés.
   Optimizan el saldo monetario minimizando los costos de corretaje de ir al banco (b) y los intereses perdidos (r):
   M^d = √(b · Y / (2r))
   - Elasticidad-ingreso: 0.5 (existen economías de escala en el uso del dinero).
   - Elasticidad-tasa de interés: -0.5 (demuestra matemáticamente la sensibilidad negativa de la demanda transaccional al interés).

4. James Tobin (1958) – Teoría de Selección de Cartera bajo Incertidumbre:
   Microfundamenta la tenencia simultánea de dinero y bonos sin asumir expectativas fijas: los inversores con aversión al riesgo diversifican entre dinero (riesgo cero, rendimiento cero) y bonos (rendimiento positivo r con riesgo de pérdida de capital medido por la varianza). Al subir r, aumenta la tenencia de bonos y se reduce la demanda de saldos monetarios.""",

            "t3_inflacion": """• POSTURA CLÁSICA VS KEYNESIANA:
Fisher y Pigou sostienen la proporcionalidad estricta entre la oferta monetaria y los precios bajo pleno empleo. Tobin formaliza la relación entre demanda agregada, costos y salarios en la síntesis neoclásica.""",

            "t4_sistema_bancario": """• INTERMEDIACIÓN FINANCIERA:
Tobin desarrolla la teoría de los intermediarios financieros: los bancos comerciales compiten con otros intermediarios emitiendo pasivos y adquiriendo activos en base a las tasas de rendimiento relativas.""",

            "t5_crisis_fluctuaciones": """• IRVING FISHER (1933) – LA TEORÍA DE LA DEFLACIÓN POR DEUDA (DEBT-DEFLATION):
Aporte histórico cumbre: Fisher explica cómo el sobreendeudamiento privado y la caída de precios desatan una espiral donde el intento de pagar deudas liquidando activos a la baja hunde más los precios, haciendo que el valor real de las deudas aumente en vez de disminuir, arrastrando a la economía a la depresión.""",

            "t6_politica_monetaria": """• REGLAS VS GESTIÓN DE TASAS:
Clásicos: Disciplina estricta del patrón oro.
Tobin: Manejo activo de la estructura temporal de tasas de interés y de la oferta de deuda pública para estimular la inversión mediante la 'q de Tobin'.""",

            "t7_expectativas_metodologia": """• MODELIZACIÓN MATEMÁTICA RIGUROSA:
Modelos de optimización de inventarios (Baumol) y análisis de media-varianza de portafolios (Tobin).""",

            "t8_represion_desarrollo": """• MERCADOS FINANCIEROS MADUROS:
[No abordan países subdesarrollados en estos textos].
Sus modelos asumen mercados de capitales desarrollados y ausencia de controles administrativos severos."""
        }
    }
]

# Analysis of texts > 40 pages (Facu 100 and Facu 97) with maximum academic rigor
deep_dive_data = {
    "title": "Análisis Crítico y Comparativo de los Textos de Más de 40 Páginas",
    "rule_applied": "En estricto cumplimiento de la consigna ('los textos de más de 40 hojas compáralo con respecto a los demás textos y solo recopila la información relacionada'), se filtraron todas las páginas tangenciales o redundantes (los debates microeconómicos marginalistas de los años 40 en Friedman y las 35 páginas de cuadros econométricos ARDL de series trimestrales argentinas en Demanda de Dinero) para consolidar únicamente los conceptos teóricos y empíricos directamente articulados con el programa de Sistemas Bancarios y Teoría Monetaria.",
    "texts": [
        {
            "id": "facu-100",
            "file": "Facu 100 Friedman-2496353.pdf",
            "author": "Milton Friedman",
            "title": "La Metodología de la Economía Positiva",
            "pages": 43,
            "core_thesis": "Una ciencia positiva no puede juzgarse por el realismo ontológico de sus supuestos, sino por la precisión empírica de sus predicciones. Los agentes económicos se comportan 'como si' conocieran y optimizaran según las ecuaciones del modelo.",
            "filtered_out": "Se descartaron más de 25 páginas dedicadas a la controversia microeconómica marginalista de los años 40 (encuestas a empresarios de Hall y Hitch en Oxford, críticas de Richard Lester y réplicas de Fritz Machlup sobre fijación de precios en competencia monopolística vs perfecta), por ser ajenas a la teoría monetaria y bancaria.",
            "retained_core": "La fundamentación epistemológica del instrumentalismo: la dicotomía positiva vs normativa, el principio del 'como si' (as if), el rechazo a evaluar teorías por la verosimilitud de sus supuestos y la primacía de la capacidad predictiva sobre la descripción institucional.",
            "cross_comparisons": [
                {
                    "linked_text": "Facu 64 (Harry Johnson)",
                    "connection": "Johnson desvela que Friedman utilizó esta exacta estrategia metodológica para doblegar al keynesianismo: reemplazó los complejos sistemas estructurales keynesianos por hipótesis monetarias simples (M → P) respaldadas en predicciones robustas."
                },
                {
                    "linked_text": "Facu 59 (Argandoña - Definición de Dinero)",
                    "connection": "Argandoña cita expresamente la metodología de Friedman (nota al pie 55): Friedman y Schwartz justifican adoptar M2 no por una esencia intrínseca del dinero, sino por ser el agregado que predice con mayor estabilidad el ingreso nominal."
                },
                {
                    "linked_text": "Facu 96 (Argandoña - Milton Friedman)",
                    "connection": "Argandoña dedica la sección inicial a este ensayo, demostrando que la hipótesis del ingreso permanente y la tasa natural de desempleo dependen conceptualmente de modelar a los agentes 'como si' optimizaran a largo plazo."
                },
                {
                    "linked_text": "Facu 108 (Guillermo Maya Muñoz)",
                    "connection": "Robert Lucas y la Nueva Macroeconomía Clásica llevan el positivismo de Friedman al extremo, exigiendo expectativas racionales y modelos de equilibrio general donde los agentes actúan 'como si' conocieran la estructura estocástica de la economía."
                },
                {
                    "linked_text": "Facu 86 (Peter Earl / G. L. S. Shackle)",
                    "connection": "Antítesis metodológica radical: Shackle y Earl rechazan el instrumentalismo de Friedman por considerar que ignorar los procesos mentales reales y tratar a las personas 'como si' fueran máquinas predictivas anula la comprensión de la incertidumbre genuina."
                }
            ]
        },
        {
            "id": "facu-97",
            "file": "Facu 97 Demanda de dinero.pdf",
            "author": "Álvaro Chaves Barea (Tutor: Alejandro Trapé)",
            "title": "Demanda de Dinero",
            "pages": 61,
            "core_thesis": "La demanda de dinero ha evolucionado desde una visión mecánica de medio de pago transaccional (Fisher) hacia la preferencia por la liquidez keynesiana y la teoría de asignación de carteras de activos bajo riesgo y rendimiento (Tobin, Friedman), culminando en modelos de huida del dinero en hiperinflaciones (Cagan).",
            "filtered_out": "Se omitieron más de 35 páginas compuestas por tablas econométricas de raíces unitarias, cointegración de Johansen, vectores de corrección de error (VEC), modelos autorregresivos con rezagos distribuidos (ARDL) y proyecciones de demanda de M2 para la República Argentina entre 1993 y 2015.",
            "retained_core": "La reconstrucción conceptual y matemática de las grandes etapas doctrinales de la demanda de saldos reales: Clásica (Fisher MV=PT), Cambridge (Pigou Md=kPY), Keynes (preferencia por la liquidez L1+L2), Baumol-Tobin (inventarios √(2bY/r)), Tobin (selección de cartera) y Friedman (Md/P = f(Yp, w, rm, rb, re, πe, u)).",
            "cross_comparisons": [
                {
                    "linked_text": "Facu 95 (Hernando Zuleta - Señoreaje)",
                    "connection": "Zuleta utiliza exactamente la función semilogarítmica de demanda de dinero en hiperinflaciones de Cagan analizada en Chaves Barea para derivar la curva de Laffer del señoreaje y calcular la tasa de inflación que maximiza la recaudación fiscal (π* = 1/α)."
                },
                {
                    "linked_text": "Facu 59 (Argandoña - Definición de Dinero)",
                    "connection": "Toda función teórica de demanda de dinero requiere una contrapartida empírica medible: si se define dinero como M1, prima el motivo transacción; si se define como M2 o M3, adquiere relevancia la rentabilidad de cuasidineros y sustitutos cercanos."
                },
                {
                    "linked_text": "Facu 108 (Guillermo Maya Muñoz)",
                    "connection": "El debate doctrinal central entre Keynes y Friedman gira en torno a la estabilidad de la función de demanda de dinero: para Keynes es inestable por los espíritus animales y la trampa de liquidez; para Friedman es la función macroeconómica más estable de la economía."
                },
                {
                    "linked_text": "Facu 174 (Banking School vs Currency School)",
                    "connection": "Para la Currency School la demanda de dinero es pasiva y la oferta causa los precios; para la Banking School la demanda de dinero comercial es la fuerza motriz endógena que determina la creación de crédito y depósitos bancarios a través de la Ley del Reflujo."
                },
                {
                    "linked_text": "Facu 66 (Ronald McKinnon)",
                    "connection": "McKinnon reformula la demanda de dinero para economías en desarrollo: demuestra que la demanda de saldos reales M2 se desploma si las tasas reales son negativas, liquidando la complementariedad entre dinero y acumulación de capital."
                }
            ]
        }
    ]
}

# We also load original 13 texts summaries from data.js or preserve them
with open("static/static_data.json", "r", encoding="utf-8") as f:
    old_data = json.load(f)

texts_data = old_data["texts"]

final_output = {
    "metadata": {
        "title": "Compendio de Sistemas Bancarios y Teoría Monetaria",
        "subtitle": "Tratado Doctrinal Exhaustivo para Evaluaciones Universitarias",
        "generated_date": "Octubre 2026",
        "total_texts": 13,
        "total_economists": len(economists_data),
        "total_topics": len(topics_data)
    },
    "topics": topics_data,
    "economists": economists_data,
    "texts": texts_data,
    "deep_dive_over_40": deep_dive_data
}

# Save in root and static
with open("static_data.json", "w", encoding="utf-8") as f:
    json.dump(final_output, f, ensure_ascii=False, indent=2)

with open("static/static_data.json", "w", encoding="utf-8") as f:
    json.dump(final_output, f, ensure_ascii=False, indent=2)

js_content = f"window.BANKING_DATA = {json.dumps(final_output, ensure_ascii=False, indent=2)};"
with open("data.js", "w", encoding="utf-8") as f:
    f.write(js_content)

with open("static/data.js", "w", encoding="utf-8") as f:
    f.write(js_content)

print("Generated exhaustive university database successfully in root and static!")

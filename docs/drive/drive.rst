:orphan:
:html_theme.sidebar_secondary.remove:
:hide-toc:

:fa:`brain` Rijden maar
########################

.. article-info::
    :author: :fa:`brain` Programmeren
    :read-time: 15 min

1
---

In de vorige workshop heb je de robot aangezet. Maar ze doet nog niets.
Ze staat nog wel steeds stil. In deze workshop leer je hoe je de
robot rond kan laten rijden en waarom niet alle motoren hetzelfde zijn.

.. video:: /_static/media/mirte_drive.mp4
   :width: 500
   :autoplay:
   :loop:


.. admonition:: LET OP
   :class: warning

   In deze workshop ga je met de robot rondrijden. Om te zorgen dat je 
   robot niet stuk gaat moet er altijd voor zorgen dat je robot op de 
   vloer staat en dus niet van je tafel afrijdt!


2
---

.. grid:: 1 2 2 2
   :gutter: 2

   .. grid-item::

      Je had het misschien al gezien, aan de rechterkant van het paneel
      vind je in het ‘besturen’ tabblad bij ‘actuatoren’ 
      ook de motoren op de motor aanzetten. De makkelijkste manier om dit te 
      doen is om op de pijltjes te klikken bij ‘Besturing’. Probeer je robot 
      maar eens een stukje te laten rijden. Met het pijltje naar boven zou 
      de robot naar voren moeten rijden.

   .. grid-item::

      .. image:: _media/drive_control.png
         :width: 350
         :alt: Drive control


.. dropdown:: :fa:`question-circle` Help

   - Als er geen enkele motor draait:
      - Controleer of de motordraadjes goed in de motor controller zitten.
      - Controleer of het lampje van de motorcontroller aan is. Als deze
        niet aan is kan je kijken of deze goed in de PCB zit. Als ook dat klopt
        kan je nog even controleren of misschien een motor controller van
        een andere robot wel werkt.
   - Als de motoren wel draaien, maar ze gaan de verkeerde kant op:
      - Het kan natuurlijk zijn dat je de draadjes van de motoren niet goed
        hebt aangesloten. Kijk hoe je de draadjes goed aan kan sluiten 
        totdat het wel goed werkt.

3
---

.. grid:: 1 2 2 2
   :gutter: 2

   .. grid-item::

      De robot zou nu een stukje moeten gaan rijden. Het kan zijn dat je robot 
      nog wat te snel gaat, of dat ze te langzaam draait. Je kan dit proberen 
      in te stellen door de snelheid en draaisnelheid aan te passen. Omdat niet 
      alle motoren hetzelfde zijn zal dit voor elke robot anders zijn. Het kan zelfs 
      zo zijn dat de beide motoren in je robot iets anders bewegen (en de robot 
      dus niet rechtdoor gaat).
 
   .. grid-item::

      .. image:: _media/drive_speed_settings.png
         :width: 350
         :alt: Drive speed settings

4
---

.. grid:: 1 2 2 2
   :gutter: 2

   .. grid-item::

      Dat beide motoren niet precies hetzelfde zijn kunnen we ook op een andere 
      manier bekijken. We kunnen de motoren namelijk ook los van elkaar aanzetten. 
      Elke motor kunnen we een waarde tussen de -100 en 100 geven.

      +------+--------------------+
      | -100 | maximaal achteruit |
      +------+--------------------+
      | 0    | stop               |
      +------+--------------------+
      | 100  | maximaal vooruit   |
      +------+--------------------+

      Elke motor is anders en zal bij een andere waarde pas beginnen met rijden. 
      Tot die tijd zal je een soort piepje horen. Dat komt omdat de motor wel wil 
      draaien, maar nog te veel weerstand voelt.

   .. grid-item::
      
      .. image:: _media/individual_motor_control.png
         :width: 350
         :alt: Drive speed settings

4
---

.. grid:: 1 2 2 2
   :gutter: 2

   .. grid-item::

      **Opdracht:** Laat de robot op de grond staan en probeer van beide 
      motoren de waardes te vinden wanneer ze beginnen te draaien.

   .. grid-item::

      +--------------------------------+-------+
      | De **linker** motor draait...  |       |
      +================================+=======+
      | ... vooruit vanaf waarde:      | . . . | 
      +--------------------------------+-------+
      | ... achteruit vanaf waarde:    | . . . |
      +--------------------------------+-------+


      +--------------------------------+-------+
      | De **rechter** motor draait... |       |
      +================================+=======+
      | ... vooruit vanaf waarde:      | . . . |
      +--------------------------------+-------+
      | ... achteruit vanaf waarde:    | . . . |
      +--------------------------------+-------+

5
---

.. grid:: 1 2 2 2
   :gutter: 2

   .. grid-item::

      **Opdracht:** Til de robot nu op van de grond en probeer van beide 
      motoren de waardes te vinden wanneer ze beginnen te draaien.

   .. grid-item::

      +--------------------------------+-------+
      | De **linker** motor draait...  |       |
      +================================+=======+
      | ... vooruit vanaf waarde:      | . . . |
      +--------------------------------+-------+
      | ... achteruit vanaf waarde:    | . . . |
      +--------------------------------+-------+


      +--------------------------------+-------+
      | De **rechter** motor draait... |       |
      +================================+=======+
      | ... vooruit vanaf waarde:      | . . . |
      +--------------------------------+-------+
      | ... achteruit vanaf waarde:    | . . . |
      +--------------------------------+-------+


6
---

Je merkt dat de waardes anders zijn als de robot op de grond staat of niet.
Als de robot op de grond staat ondervindt ze wrijving van de grond, waardoor
de motor beter zijn best moet doen voordat deze gaat draaien. 

Maar zoals je misschien ook gezien hebt kunnen deze waardes ook per motor
iets anders zijn. Elke motor is weer anders en zal bij een iets andere waarde
starten. 

Maar ook de batterij kan hier invloed op hebben. Het kan dus zijn dat de waardes
ook anders zijn als de batterij minder vol is.

.. admonition:: TIP
   :class: hint

   Het beste is dus om te zorgen dat je batterij altijd goed opgeladen is.


6
---

.. grid:: 1 2 2 2
   :gutter: 2

   .. grid-item::

      Uiteraard kan je de robot ook zelf programmeren. Hiervoor kan je naar het 
      ‘Programmeren’ tabblad. Bij ‘acties’ zie je ‘Zet snelheid van motor links 
      op 0’ staan. Deze kan je gebruiken om de robot te laten rijden.


   .. grid-item::

      .. tab-set::

         .. tab-item:: Blokken
            :sync: blokken

            .. image:: _media/motor_blockly.png
               :width: 350
               :alt: Drive with Blockly

         .. tab-item:: Python
            :sync: python

            .. image:: _media/motor_python.png
               :width: 350
               :alt: Drive with Python


7
---

.. grid:: 1 2 2 2
   :gutter: 2

   .. grid-item::

      Als je tevreden bent over wat je gemaakt hebt kan je de robot laten doen wat daar 
      staat door op de ‘play’ knop te drukken. De robot gaat dan als het goed is bewegen.

   .. grid-item::

      .. image:: _media/play_button.png
         :width: 70
         :alt: Play button

.. dropdown:: :fa:`question-circle` Help

   - Als de robot niet rijdt:
      - Dat klopt en wordt uitgelegd in de volgende stap.

8
---

.. grid:: 1 2 2 2
   :gutter: 2

   .. grid-item::

      Als je de robot het programma nu uit laat voeren zal je merken dat de robot 
      niet echt vooruit komt. Dit komt omdat we de robot haar motoren laten stoppen 
      zodra het programma klaar is. Met moeten dus nog tegen de robot zeggen dat ze 
      niet meteen hoeft te stoppen.

   .. grid-item::

      .. image:: _media/drive_seconds.png
         :width: 350
         :alt: Drive

9
---

**Opdracht:** Probeer nu de robot zo te programmeren zodat ze een vierkantje gaat 
rijden. Of een rondje?

Met ‘wacht x seconden’ kan je ook de grootte van het vierkant veranderen.
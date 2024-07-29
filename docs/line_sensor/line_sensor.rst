:orphan:
:html_theme.sidebar_secondary.remove:
:hide-toc:

:fa:`eye` Licht meten
#####################

.. article-info::
    :author: :fa:`eye` Sensoren
    :read-time: 30 min

1
---

Om de robot iets slims te laten doen zal de robot ook iets van haar omgeving 
waar moeten nemen. Dit kan een robot doen door gebruik te maken van sensoren. 
In deze workshop leer je hoe de robot licht kan meten en hierdoor bijvoorbeeld 
een zwarte lijn kan herkennen.

2
---

.. grid:: 1 2 2 2
   :gutter: 2

   .. grid-item::

      Om te weten wat er om de robot heen gebeurt heeft de robot sensoren. Mensen 
      en dieren hebben dat ook, alleen noemen we het dan zintuigen. Omdat een 
      robot natuurlijk anders werkt kan de robot ook andere din>
      .. TODO: wat moet hier staan???

      Om de waarden van de sensoren te kunnen zien moet je naar het juist tabblad 
      toe gaan. Dit kan zowel in het tabblad ‘Besturen’, als in het tabblad 
      ‘Programmeren’.


   .. grid-item::

      .. image:: _media/sensors_tab.png
         :width: 350
         :alt: Sensoren

3
---

.. grid:: 1 2 2 2
   :gutter: 2

   .. grid-item::

      **Opdracht:** In deze workshop gaan we kijken naar de lichtsensor. Als je goed kijkt zie 
      je dat deze sensor twee bolletjes heeft met een schotje daar tussen. Het ene 
      bolletje is eigenlijk een klein lampje wat infrarood licht uitzendt. Het 
      andere bolletje is echt de sensor. Die meet hoeveel van het infrarode licht 
      er gemeten wordt. Zet de robot maar eens op een tafel en kijk wat de waarde 
      van de sensor is. Hou vervolgens maar eens je vinger over de twee bolletjes 
      en kijk wat de waarde nu is.

   .. grid-item::

      +-------------------+-------+
      | Waar:             |       |
      +===================+=======+
      | op tafel:         | . . . |
      +-------------------+-------+
      | op vloer:         | . . . |
      +-------------------+-------+
      | vinger op sensor: | . . . |
      +-------------------+-------+
      | op.......:        | . . . |
      +-------------------+-------+

.. admonition:: LET OP
   :class: warning

   Ondanks dat je robot stil op tafel staat zal de waarde van de sensor toch elke 
   keer wat anders zijn. Dit komt omdat de sensor heel nauwkeurig is, maar ook omdat 
   er soms kleine foutjes gemaakt worden door de sensor. Die foutjes noemen we ‘ruis’ 
   (of ‘noise’ in het Engels).

4
---

.. grid:: 1 2 2 2
   :gutter: 2

   .. grid-item::

      **Opdracht:** Probeer te achterhalen wat de grootste (maximale) en de kleinste 
      (minimale) waardes van deze sensor zijn.

   .. grid-item::

      +-------------------+-------+
      | minimale waarde:  | . . . |
      +-------------------+-------+
      | maximale waarde:  | . . . |
      +-------------------+-------+


4
---

.. grid:: 1 2 2 2
   :gutter: 2

   .. grid-item::

      Deze sensor heeft een minimale waarde van 0 en een maximale waarde van 4095. 
      Zoals in opdracht 1 uitgelegd meet de sensor hoeveel infrarood licht er teruggekaatst 
      wordt.

      Als de waarde laag is, is er veel teruggekaatst. Het oppervlakte zal dus licht 
      van kleur zijn.

      Als de waarde hoog is, is er weinig teruggekaatst. Dit kan komen doordat het oppervlakte 
      niets heeft teruggekaatst en donker van kleur is.


   .. grid-item::

      .. image:: _media/line_sensor_theory.png
         :width: 350
         :alt: Line volg sensor

.. admonition:: LET OP
   :class: warning

   Het kan natuurlijk ook zijn dat de robot helemaal niet naar een oppervlakte kijkt.

   De waarde kan ook laag zijn als er op een andere manier (infrarood) licht op de sensor 
   komt door bv de zon of een lamp.

   De waarde kan ook hoog zijn als het licht helemaal niet terug komt en de sensor bv te ver 
   van een vloer af is.

.. admonition:: INFO
   :class: note

   De maximale waarde die uit deze sensor komt is eigenlijk niet afhankelijk van de sensor, 
   maar van de microcontroller. Die vertaalt de waarde van de sensor (in Volt) naar een
   waarde die we hier zien.


5
---

.. grid:: 1 2 2 2
   :gutter: 2

   .. grid-item::

      Het uitlezen van de sensor kunnen we ook doen vanuit het ‘programmeer’ tabblad.

      Maak met een combinatie van blokken in ‘sensoren’ en ‘acties’ het volgend blok en 
      druk op ‘play’ rechtsboven.

      Je ziet nu rechtsonder wat de waarde van de linker sensor op dat moment was. Net als 
      bij de motor stopt het programma dus meteen nadat het klaar zie je de waarde dus maar 
      1 keer.


   .. grid-item::

      .. tab-set::

         .. tab-item:: Blokken
            :sync: blokken

            .. image:: _media/line_sensor_blockly.png
               :width: 350
               :alt: Line volg sensor Blockly

         .. tab-item:: Python
            :sync: python

            .. image:: _media/line_sensor_python.png
               :width: 350
               :alt: Line volg sensor Python








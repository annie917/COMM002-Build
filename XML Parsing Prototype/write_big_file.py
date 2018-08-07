#!/usr/local/bin/python3.6

import configparser

# Program to create an XML file containing n plant records

config = configparser.ConfigParser()

config.read('./config.ini')

n = int(config['TimeTests']['number_of_plants'])

f = open('big_xml.xml', 'w')

f.write('<?xml version="1.0" encoding="utf-8"?>\n')
f.write('<AllEntityDetails xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" '
        'xmlns:xsd="http://www.w3.org/2001/XMLSchema">\n')

for i in range(n):

    f.write('<EntityDetails>\n')
    f.write('<EntityDetailsItems '
            'PlantEntityId="1589" '
            'PreferredCommonName="PCN ' + str(i+1) + '" '
            'AcceptedBotanicalName="&lt;em&gt;Ranunculus&lt;/em&gt; &lt;em&gt;aconitifolius&lt;/em&gt; '
            '\'Flore Pleno\' (d) AGM" '
            'Name_Num="' + str(i+1) + '" '
            'PerfectForPollination="false" '
            'Family="Ranunculaceae" '
            'Genus="Ranunculus" '
            'PlantImagePath="http://vsorchard/PlantFinderPlus_Test/PlantEntityImages/WSY0034793_4502.jpg" '
            'ImageCopyRight="RHS 2002" '
            'EntityDescription="\'Flore Pleno\' is a vigorous herbaceous perennial to 90cm, with '
            'palmately divided dark green leaves and branched stems bearing long-lasting double, button-like white '
            'flowers 2cm in width" GenusDescription="&lt;em&gt;Ranunculus&lt;/em&gt; can be annuals, biennials, '
            'evergreen or herbaceous perennials, with rhizomes, tubers or spreading by runners. The leaves are '
            'variable but often palmately lobed or dissected and the flowers usually bowl-shaped" '
            'PlantType="Herbaceous Perennial" '
            'Foliage="Deciduous" '
            'SuggestedPlantUses="Cottage/Informal Garden, Flower borders and beds or Cut Flowers" '
            'Awards="Award of Garden Merit" '
            'Habit="Clump-forming" '
            'Fragrance="" '
            'Height="0.5-1 metres" '
            'Spread="0.1-0.5 metres" '
            'TimeToFullHeight="2-5 years" '
            'SoilType="Clay, Loam or Chalk" '
            'Moisture="Moist but well-drained" '
            'PH="Acid, Alkaline or Neutral" '
            'Hardiness="H7 (very hardy)" '
            'Aspect="South-facing, East-facing or West-facing" '
            'Exposure="Sheltered" '
            'Sunlight="Full Sun, Partial Shade" '
            'Cultivation="Grow in humus-rich, fertile, moist or moist but well-drained soil in full or partial shade" '
            'PestResistance="Generally pest free" '
            'DiseaseResistance="May be subject to &lt;a href=\'http://www.rhs.org.uk/advicesearch/Profile.aspx?'
            'pid=253\' &gt;powdery mildews&lt;/a&gt; in dry conditions" '
            'Pruning="No pruning required" '
            'Toxicity="" '
            'Propagation="Propagate by &lt;a href=\'http://www.rhs.org.uk/advicesearch/Profile.aspx?pid=363\' '
            '&gt;division&lt;/a&gt; in autumn" '
            'Flower="White in Spring and  Summer" '
            'FoliageColour="Dark Green in Autumn, Spring and  Summer" '
            'Stem="" '
            'Fruit="" '
            'Leaf="" '
            'Native="False" '
            'LowMaintenance="False" '
            'SupplierURL="http://apps.rhs.org.uk/rhsplantfinder/pfregions.asp?ID=97224" HortGroupDescription="">\n')
    f.write('<CommonNames>\n')
    f.write('<CommonName>fair maids of France</CommonName>\n')
    f.write('<CommonName>fair maids of Kent</CommonName>\n')
    f.write('</CommonNames>\n')
    f.write('<Synonyms>\n')
    f.write('<Synonyms>&lt;em&gt;Ranunculus&lt;/em&gt; &lt;em&gt;aconitifolius&lt;/em&gt;  &lt;em&gt;flore&lt;/em&gt;  '
            '&lt;em&gt;pleno&lt;/em&gt; \'Batchelor\'s Button\'</Synonyms>\n')
    f.write('</Synonyms>\n')
    f.write('</EntityDetailsItems>\n')
    f.write('</EntityDetails>\n')

f.write('</AllEntityDetails>\n')


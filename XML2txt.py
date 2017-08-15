from numpy import *
import xml.etree.ElementTree as et

                
new_set=[]
tree = et.parse('c17.xml')
cards = tree.getroot()
#cards = cards[1]

i=1
f=open('C17.txt','w')
for card in cards:
    new_set.append({})
    for field in card:
        new_set[-1][field.tag]=field.text
        
    #Account for gold cards with multiple color fields
    if [field.tag for field in card].count('color')>1:
        new_set[-1]['color']='Gld'
        
    #Print Card name
    print >>f, 'Card Name:\t%s' % new_set[-1]['name'] #Print all card names
        
    #Print card color
    if 'Artifact' in new_set[-1]['type']:
        new_set[-1]['color']='Art'
        print >>f, 'Card Color:\tArt'  #Set color to Art for artifacts
    elif 'Land' in new_set[-1]['type']:
        new_set[-1]['color']='Lnd'
        print >>f, 'Card Color:\tLnd' #Set color to Lnd for lands
    else:
        print >>f, 'Card Color:\t%s' % new_set[-1]['color']
                
    #Print card mana cost    
    try:
        print >>f, 'Mana Cost:\t%s' % new_set[-1]['manacost']
    except KeyError:
        print >>f, 'Mana Cost:'
        
    #Print card type
    print >>f, 'Type & Class:\t%s' % new_set[-1]['type']
    
    #Print card P/T
    try:
        print >>f, 'Pow/Tou:\t%s' % new_set[-1]['pt']
    except KeyError:
        print >>f, 'Pow/Tou:'
        
    #Print card text, rarity, and number
    print >>f, 'Card Text:\t%s' % new_set[-1]['text']
    print >>f, 'Rarity:'
    print >>f, 'Card #:\t\t%i/%i' % (i,len(cards))
    print >>f, ''
    
    i+=1
    
f.close()
    
    












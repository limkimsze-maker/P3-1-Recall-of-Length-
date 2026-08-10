from pathlib import Path
import re

p=Path('index.html')
s=p.read_text(encoding='utf-8')

new_objects='''const unitObjects=[
{name:"classroom doorway",type:"door",value:2,unit:"m",dimension:"height"},
{name:"sports bottle",type:"bottle",value:23,unit:"cm",dimension:"height"},
{name:"coloured pencil",type:"pencil",value:18,unit:"cm",dimension:"length"},
{name:"study table",type:"table",value:1,unit:"m",dimension:"length"},
{name:"measuring ruler",type:"ruler",value:30,unit:"cm",dimension:"length"},
{name:"single bed",type:"bed",value:2,unit:"m",dimension:"length"},
{name:"young tree",type:"tree",value:3,unit:"m",dimension:"height"},
{name:"park lamp post",type:"lamp",value:6,unit:"m",dimension:"height"},
{name:"sports hall entrance",type:"school",value:8,unit:"m",dimension:"height"},
{name:"activity-room floor line",type:"corridor",value:5,unit:"m",dimension:"length"}
];'''
s,n=re.subn(r'const unitObjects=\[.*?\];\nconst structures=',new_objects+'\nconst structures=',s,count=1,flags=re.S)
if n!=1: raise SystemExit('unitObjects not replaced')

new_est='''const estimates=[
{name:"sports bottle",type:"bottle",measure:"Height ?",q:"Which is the most sensible height of a sports bottle?",ans:"23 cm",ops:["23 cm","23 m","230 m","2 m"]},
{name:"classroom doorway",type:"door",measure:"Height ?",q:"Which is the most sensible height of a classroom doorway?",ans:"2 m",ops:["2 m","2 cm","20 cm","20 m"]},
{name:"study table",type:"table",measure:"Length ?",q:"Which is the most sensible length of a study table?",ans:"1 m",ops:["1 m","1 cm","10 m","100 m"]},
{name:"measuring ruler",type:"ruler",measure:"Length ?",q:"Which is the most sensible length of a classroom measuring ruler?",ans:"30 cm",ops:["30 cm","30 m","3 m","300 m"]},
{name:"single bed",type:"bed",measure:"Length ?",q:"Which is the most sensible length of a single bed?",ans:"2 m",ops:["2 m","2 cm","20 cm","20 m"]}
]'''
s,n=re.subn(r'const estimates=\[.*?\];shuffle\(estimates\)',new_est+';shuffle(estimates)',s,count=1,flags=re.S)
if n!=1: raise SystemExit('estimates not replaced')

p.write_text(s,encoding='utf-8')

from random import shuffle

USERS = [
    "admin",
    "corentin.colin",
    "dorian.meyer",
    "rachel.aubert",
    "malo.nguyen",
    "benjamin.legrand3",
    "albane.leclercq",
    "ryan.lacroix",
    "ilan.giraud",
    "corentin.lemaire1",
    "lilou.charles",
    "elya.deschamps",
    "soren.lefebvre",
    "laurine.dupuis1",
    "naomi.bonnet",
    "manon.riviere",
    "owen.muller",
    "damien.da-silva2",
    "sophia.dupont",
    "victoire.noel",
    "jules.lemoine1",
    "clea.perez",
    "heloise.perrin",
    "nael.gerard",
    "nina.francois",
    "celian.meyer",
    "titouan.simon",
    "fanny.gauthier",
    "inaya.noel",
    "alex.aubert",
    "clara.colin",
    "flora.fleury",
    "thomas.moreau1",
    "maelia.fleury",
    "clemence.dumont",
    "jade.schmitt",
    "sohan.jean",
    "matthieu.louis",
    "alice.mathieu",
    "morgane.lemaire2",
    "tristan.pierre",
    "lucie.guillot",
    "solene.picard",
    "nils.nguyen",
    "charline.fontai",
    "pauline.vidal1",
    "martin.moreau1",
    "lise.david",
    "lino.roussel",
    "thais.giraud",
    "remi.duval",
    "candice.henry",
    "adam.arnaud",
    "lenny.renaud",
    "leonard.moulin",
    "fanny.dumas",
    "nina.guillaume",
    "maelys.blanc1",
    "meline.vidal",
    "maya.leclerc",
    "justine.mathieu",
    "elise.denis1",
    "soan.meyer",
    "louane.noel",
    "lea.brun2",
    "elea.petit",
    "enola.marchand",
    "melissa.charles",
    "livia.fabre",
    "nora.brun",
    "garance.dupont",
    "leonard.roger",
    "isaac.renaud",
    "claire.fleury1",
    "martin.rey",
    "soan.martinez",
    "maxence.muller2",
    "mae.aubert",
    "emilie.roche1",
    "marine.gonzalez1",
    "clemence.deschamps",
    "come.aubert",
    "candice.roux",
    "romeo.gauthier",
    "adam.schmitt",
    "louna.colin",
    "giulia.blanchard",
    "selene.jean",
    "lyna.denis",
    "norah.roy",
    "noelie.faure",
    "evan.chevalier",
    "laura.rodriguez",
    "sandra.faure",
    "alice.perez",
    "clara.girard2",
    "faustine.perrin",
    "coline.andre1",
    "angele.denis1",
    "oscar.brunet",
    "anais.joly1",
    "eline.lucas",
    "marion.dumas",
    "maelya.le-gall",
    "eloise.roy1",
    "mathias.sanchez",
    "gauthier.leclercq",
    "romeo.morel",
    "hadrien.dumas",
    "thomas.nguyen",
    "clement.noel2",
    "fabien.dupuis",
    "marion.blanc",
    "elena.rey",
    "teo.adam",
    "elisa.colin",
    "lia.blanchard",
    "julien.pierre1",
    "daphne.lefebvre",
    "basile.brunet",
    "pauline.rodriguez",
    "cassandra.leroy",
    "lia.sanchez",
    "roxane.olivier",
    "louane.leclercq",
    "laurine.garnier1",
    "baptiste.leroy2",
    "marie.gautier4",
    "owen.sanchez",
    "laly.roy",
    "maeline.gaillard",
    "claire.lacroix",
    "flora.guillot",
    "kelya.bourgeois",
    "gauthier.roux",
    "alix.joly",
    "lou.olivier",
    "clarisse.perrin",
    "bastien.boyer",
    "nael.fleury",
    "ezio.duval",
    "garance.da-silva",
    "chiara.adam",
    "elise.brun",
    "selena.fontai",
    "victor.le-gall",
    "noe.carpentier",
    "julien.berger",
    "marine.martin",
    "rachel.roche",
    "luna.martin",
    "margot.fontai",
    "adam.philippe",
    "juliette.renard",
    "noemie.guillot",
    "amelie.morel1",
    "laly.rolland",
    "ilan.henry",
    "abel.dupuis",
    "maya.boyer",
    "maelys.guillot",
    "alyssia.joly",
    "lucien.blanchard",
    "cassandre.le-gall",
    "sara.deschamps",
    "lola.aubert",
    "martin.dufour",
    "lola.blanc",
    "morgane.muller",
    "julie.henry",
    "loan.arnaud",
    "lia.guerin",
    "inaya.marie",
    "zoe.leroy1",
    "leandro.dupont",
    "louane.bertrand",
    "claire.roger1",
    "anais.perrin",
    "antonin.menard",
    "romy.fleury",
    "livio.robert",
    "loane.joly",
    "ethan.fontai",
    "giulia.simon",
    "nolhan.dumont",
    "florian.louis2",
    "lucy.richard",
    "capucine.morel",
    "william.roger",
    "zoe.arnaud",
    "timeo.david",
    "margot.bertrand",
    "sacha.vidal",
    "lucile.bourgeois",
    "milan.mathieu",
    "maya.nguyen",
    "luka.nguyen",
    "maxime.brun",
    "anthony.giraud1",
    "edgar.dupont",
    "lilly.laurent",
    "leandro.roy",
    "lison.rodriguez",
    "marceau.renard",
    "mathieu.faure",
    "livio.roussel",
    "sophie.roussel",
    "dorian.petit",
    "emeline.fabre",
    "clemence.guerin",
    "norah.fernandez",
    "laurine.guillot",
    "victoire.francois",
    "tessa.gonzalez",
    "aurore.arnaud",
    "roxane.nguyen",
    "nils.roy",
    "mathias.marchand",
    "andrea.garcia",
    "celestine.aubert",
    "angelina.berger",
    "livia.pierre",
    "martin.louis",
    "hadrien.louis",
    "thibaut.martinez",
    "amelia.riviere",
    "celestine.leclerc",
    "maelyne.roche",
    "emeline.jean",
    "enzo.schmitt",
    "olivia.deschamps",
    "alicia.pierre",
    "loris.bertrand",
    "jeanne.arnaud",
    "soren.renaud",
    "timothe.blanc",
    "stella.leclerc",
    "maelle.da-silva",
    "lison.gaillard",
    "elena.durand",
    "alice.joly",
    "clarisse.menard",
    "maelyne.lecomte",
    "solene.olivier",
    "noemie.fontai",
    "giulia.vidal",
    "johan.moreau",
    "louis.morin1",
    "lily.gauthier",
    "alexia.chevalier",
    "jonas.faure",
    "morgan.girard",
    "maelie.renard",
    "helena.henry",
    "eloane.picard",
    "naomi.lambert",
    "matheo.muller",
    "leandre.francois",
    "louanne.roche",
    "lilian.roux",
    "hugo.martin2",
    "aaron.mercier",
    "louna.pierre",
    "romain.dupuis",
    "lucy.guerin",
    "joshua.joly",
    "sara.chevalier",
    "zoe.fleury",
    "eliott.clement",
    "laura.lambert2",
    "lola.dumont1",
    "lise.pierre1",
    "livio.dupuis",
    "maely.boyer",
    "hanae.leclerc",
    "rachel.gauthier2",
    "diego.carpentier",
    "apolline.jean",
    "paul.muller",
    "andrea.roy",
    "manon.faure",
    "pauline.petit",
    "melody.le-gall",
    "victoria.fleury",
    "nolhan.roche",
    "teo.renard",
    "elias.moreau2",
    "gabrielle.dupuis",
    "aaron.mathieu",
    "johan.aubert",
    "florian.rolland",
    "selena.renard",
    "ambre.moreau2",
    "aurelien.robin2",
    "laura.giraud",
    "romain.da-silva2",
    "nora.renard",
    "maya.boyer1",
    "kenzo.lefevre",
    "lilly.guillaume",
    "damien.noel1",
    "isaac.jean",
    "hector.brunet",
    "timothe.menard",
    "noam.fontai",
    "gaetan.olivier",
    "maxence.berger",
    "victoria.rousseau",
    "lia.fabre",
    "lilou.guillot",
    "camille.dubois",
    "camille.perez",
    "thibaut.boyer",
    "matthieu.guillot",
    "marie.masson1",
    "marceau.gautier",
    "william.moulin1",
    "tim.leroux",
    "nils.garcia",
    "romy.roussel",
    "noam.caron",
    "lucy.renard",
    "noah.rousseau",
    "mathias.lopez",
    "mae.chevalier",
    "alexia.bonnet",
    "anaelle.carpentier",
    "fabio.le-gall",
    "anaelle.roger",
    "diego.robert",
    "lison.blanchard",
    "lya.lemaire",
    "solene.blanc",
    "angelo.bertrand",
    "loane.michel",
    "justine.fabre",
    "meline.roux1",
    "flavie.durand1",
    "flavie.gonzalez",
    "noa.pierre",
    "nina.leclerc",
    "aubin.vidal",
    "oscar.francois",
    "gabriel.fournier",
    "maiwenn.fabre",
    "raphael.durand",
    "elia.roussel",
    "bastien.lefevre",
    "sandra.bonnet",
    "enora.mathieu",
    "basile.garcia",
    "selene.guillot",
    "tessa.denis",
    "nolan.meyer",
    "timothee.lopez",
    "chloe.laurent6",
    "mathieu.bourgeois1",
    "candice.girard2",
    "timothe.lacroix",
    "romane.bonnet",
    "loan.gonzalez",
    "mathys.renard",
    "yanis.lopez",
    "lise.fontai",
    "malo.moreau",
    "erwan.faure",
    "isaac.marchand",
    "tessa.chevalier",
    "lena.fontai",
    "nino.da-silva",
    "alyssia.moreau",
    "louka.chevalier",
    "eleonore.gautier",
    "cleo.nguyen",
    "loris.lambert",
    "titouan.michel",
    "fabio.garnier",
    "charlotte.dumas1",
    "louison.adam",
    "nolhan.colin",
    "margot.louis",
    "alizee.leclerc",
    "gabrielle.martin1",
    "helena.adam",
    "luca.fernandez",
    "kylian.denis",
    "ethan.da-silva",
    "celestine.marchand",
    "marie.muller",
    "maelya.jean",
    "chloe.hubert",
    "emma.fournier",
    "maelya.gonzalez",
    "morgane.rey",
    "eloane.fabre",
    "remy.moulin",
    "louise.dubois",
    "romain.le-gall1",
    "logan.roy",
    "elia.leroy",
    "david.roche1",
    "alice.giraud",
    "elisa.roussel",
    "lucie.arnaud",
    "tim.garnier",
    "evan.fabre",
    "liam.perez",
    "mathilde.dumas",
    "louane.michel",
    "jade.garnier3",
    "alex.garnier",
    "nathan.barbier",
    "kiara.michel",
    "lyam.jean",
    "luis.moreau",
    "leandre.deschamps",
    "nael.mercier",
    "romeo.pierre",
    "lila.barbier",
    "soline.moreau",
    "lenny.giraud",
    "gael.marie",
    "raphael.mathieu",
    "livio.faure",
    "nils.guillot",
    "louison.philippe",
    "joshua.roux",
    "kylian.garcia",
    "emmy.nguyen",
    "maelie.faure",
    "alexia.adam",
    "lya.thomas",
    "tiago.hubert",
    "leo.legrand",
    "alyssa.perrin",
    "rachel.duval2",
    "eden.nicolas",
    "emy.clement",
    "lucy.muller",
    "romane.girard1",
    "matteo.blanc",
    "inaya.rodriguez",
    "inaya.meunier",
    "aymeric.legrand",
    "marine.dupont",
    "julien.mercier1",
    "lana.roussel",
    "capucine.joly",
    "nolhan.thomas",
    "antonin.berger",
    "aubin.schmitt",
    "leonard.perrin",
    "lois.schmitt",
    "maiwenn.roussel",
    "noelie.durand",
    "celia.gerard1",
    "agathe.roche",
    "malone.marchand",
    "jade.louis",
    "pauline.schmitt",
    "marion.hubert",
    "eloane.philippe",
    "eloise.morin",
    "malo.barbier",
    "lison.denis1",
    "leana.da-silva",
    "rayan.bernard",
    "nils.chevalier",
    "quentin.legrand",
    "alban.francois",
    "marine.dumas",
    "luna.picard",
    "luka.meunier",
    "louane.leroux1",
    "lylou.fournier",
    "romy.dubois",
    "alexis.meyer",
    "valentin.nguyen1",
    "maeline.jean",
    "enola.charles",
    "julia.vidal",
    "celestine.boyer",
    "aaron.perez",
    "lorenzo.marchand",
    "morgane.lambert",
    "emilie.vincent",
    "constance.vincent",
    "apolline.vidal",
    "elsa.giraud",
    "capucine.dumont",
    "kelya.fontai",
    "mae.petit",
    "ruben.philippe",
    "maelle.lopez",
    "clea.mathieu",
    "lyam.berger",
    "erwan.renaud",
    "rachel.leroy",
    "fabio.meyer",
    "rayan.durand",
    "isaac.blanc",
    "elouan.roux",
    "clara.charles",
    "margot.lacroix",
    "norah.morin",
    "oceane.gauthier1",
    "alexandre.legrand4",
    "yanis.bertrand",
    "albane.marchand",
    "ryan.henry",
    "inaya.gerard",
    "raphael.pierre",
    "lino.hubert",
    "elia.roger",
    "eloise.olivier",
    "charline.riviere",
    "angele.dupont",
    "lyna.leroy",
    "lucas.louis1",
    "aaron.robin",
    "ilan.dufour",
    "capucine.leclercq",
    "juliette.leroy",
    "valentin.rodriguez3",
    "line.duval",
    "leo.morin1",
    "capucine.le-gall",
    "louisa.roche",
    "luka.roussel",
    "nael.arnaud",
    "jonas.garnier",
    "marius.francois",
    "matheo.nicolas",
    "charles.noel",
    "quentin.rousseau2",
    "manon.muller",
    "agathe.girard3",
    "romeo.brun",
    "nolan.francois",
    "angelina.boyer",
    "louisa.moulin",
    "ezio.girard",
    "heloise.morel",
    "logan.bertrand",
    "louis.muller",
    "maeline.rey",
    "victoria.lambert",
    "inaya.guillaume",
    "enzo.dubois",
    "antonin.chevalier",
    "justine.gaillard",
    "nolhan.lopez",
    "raphael.berger",
    "elisa.adam",
    "constance.menard",
    "ezio.schmitt",
    "thibault.arnaud",
    "kais.lucas",
    "marilou.chevalier",
    "timothee.nicolas",
    "emy.perez",
    "alexandre.rey",
    "eloane.masson",
    "louisa.boyer",
    "samuel.blanchard",
    "abel.dufour",
    "erwan.menard",
    "tessa.guillot",
    "liam.menard",
    "lola.lacroix1",
    "owen.dumas",
    "axelle.da-silva",
    "quentin.noel3",
    "basile.chevalier",
    "emmy.vincent",
    "elia.arnaud",
    "lea.bertrand2",
    "lucy.lacroix",
    "andrea.jean",
    "noemie.robin1",
    "louna.bourgeois",
    "lisa.legrand",
    "jade.durand1",
    "noemie.guillot1",
    "alexis.lacroix1",
    "selena.joly",
    "julien.durand2",
    "mila.lemaire",
    "sarah.morin",
    "elisa.robin1",
    "cassandra.brunet",
    "marceau.dupuis",
    "ambre.bernard",
    "elise.guerin",
    "eliot.menard",
    "pauline.mathieu",
    "hadrien.leroy",
    "simon.marchand",
    "louison.moreau1",
    "pierre.lambert4",
    "sasha.fournier1",
    "lena.dumas",
    "lyam.le-gall",
    "rafael.roy",
    "julia.laurent",
    "adele.denis",
    "constance.charles",
    "mathilde.brunet1",
    "gabin.perrin",
    "elea.morin",
    "elouan.andre",
    "margaux.picard",
    "matheo.aubert",
    "celestine.fabre",
    "baptiste.blanc2",
    "pauline.nguyen",
    "logan.sanchez",
    "tess.schmitt",
    "jules.da-silva",
    "elia.riviere",
    "lino.richard",
    "noelie.perrin",
    "maelyne.schmitt",
    "romain.marie",
    "mael.charles",
    "ezio.perrin",
    "anais.menard1",
    "samuel.aubert",
    "sarah.arnaud",
    "margaux.meunier",
    "hadrien.girard",
    "timeo.dubois",
    "agathe.boyer",
    "enora.gaillard",
    "ruben.aubert",
    "eliot.gauthier1",
    "celia.meunier1",
    "tessa.robin",
    "angele.dufour",
    "eline.charles",
    "elya.garnier",
    "maelys.simon",
    "emeline.morin",
    "nael.leclercq",
    "augustin.joly",
    "milo.vidal",
    "celestine.garcia",
    "capucine.giraud",
    "yann.sanchez1",
    "alyssa.francois",
    "claire.barbier4",
    "eve.sanchez",
    "justine.fournier",
    "antonin.menard1",
    "amelia.blanchard",
    "noelie.carpentier",
    "oceane.arnaud",
    "line.charles",
    "valentina.simon",
    "gabin.dupuis",
    "noam.legrand",
    "lou.dufour",
    "soan.michel",
    "ethan.moreau1",
    "jeanne.francois",
    "romane.philippe",
    "cassandre.guillaume",
    "sophia.dumas",
    "enola.olivier",
    "claire.durand",
    "aurelien.leclercq",
    "margot.lopez",
    "ana.lefevre",
    "milan.moreau",
    "giulia.andre",
    "albane.chevalier",
    "malone.riviere",
    "teo.charles",
    "luka.rodriguez",
    "quentin.leroux",
    "charlotte.noel",
    "mya.philippe",
    "manon.fleury",
    "remi.duval2",
    "timothee.simon",
    "enora.vincent",
    "mathis.guillaume",
    "emilie.lefebvre1",
    "elia.thomas",
    "edouard.marie",
    "faustine.pierre",
    "garance.guillot",
    "paul.olivier1",
    "evan.garcia1",
    "axel.philippe",
    "aymeric.louis",
    "luka.duval",
    "justine.lecomte",
    "rafael.leroux",
    "noah.perez",
    "morgan.garnier",
    "charline.lemaire",
    "maelya.gerard",
    "lou.lopez",
    "candice.morin",
    "florian.muller",
    "alice.duval1",
    "sasha.guerin",
    "lila.bourgeois",
    "louanne.noel",
    "louis.simon",
    "milan.deschamps",
    "elisa.marchand1",
    "clementine.lucas",
    "augustin.gonzalez",
    "andrea.noel",
    "eva.david",
    "lison.roussel",
    "charles.duval1",
    "alice.martinez",
    "charles.masson3",
    "enzo.vidal",
    "elena.picard",
    "gael.dufour",
    "loane.le-gall",
    "melvin.guillot",
    "noe.dupont1",
    "eline.vidal",
    "rachel.leclercq",
    "matthieu.noel",
    "arthur.lambert",
    "rafael.dupont",
    "mahe.deschamps",
    "tim.david",
    "alizee.joly",
    "noham.philippe",
    "enzo.muller",
    "garance.fleury",
    "elise.moreau4",
    "stella.durand",
    "dorian.laurent",
    "ruben.denis",
    "sasha.francois",
    "selene.fournier",
    "lily.gerard",
    "edgar.lefevre",
    "mathias.bourgeois",
    "ilan.moulin",
    "marion.barbier",
    "marius.gaillard",
    "jonas.nicolas",
    "celestin.durand",
    "leandre.lefevre",
    "clemence.dumas4",
    "alexia.robert",
    "paul.dupuis",
    "elisa.moreau2",
    "loane.joly1",
    "sandro.leclerc",
    "ava.rodriguez",
    "naomi.perez",
    "selene.faure",
    "erwan.louis",
    "justin.hubert",
    "aaron.leroux",
    "nicolas.durand8",
    "teo.berger",
    "louis.deschamps3",
    "tom.leroux1",
    "sacha.moreau",
    "gabin.lacroix",
    "pauline.le-gall1",
    "lenny.dubois1",
    "amelia.moulin",
    "auguste.fournier",
    "eden.nguyen",
    "emilie.lefebvre2",
    "lohan.sanchez",
    "capucine.chevalier",
    "matheo.faure",
    "louise.riviere",
    "lina.vincent",
    "sandro.henry",
    "tiago.renaud",
    "marion.renaud",
    "celestine.roussel",
    "lana.meunier",
    "aubin.meyer",
    "nolan.moreau",
    "celestine.legrand",
    "giulia.dufour",
    "enola.carpentier",
    "soan.renard",
    "maely.durand",
    "mila.fournier",
    "marilou.perez",
    "matheo.leclercq",
    "manon.robert3",
    "clemence.henry",
    "melissa.aubert",
    "cassandra.rodriguez",
    "alois.gautier",
    "juliette.morel1",
    "leon.moreau",
    "logan.joly",
    "clea.laurent",
    "melissa.robin1",
    "hadrien.adam",
    "timothe.menard1",
    "maeline.rey1",
    "eleonore.masson",
    "melina.legrand",
    "raphael.legrand",
    "elia.masson",
    "eliott.roche",
    "zoe.dumont",
    "lyam.arnaud",
    "mya.pierre",
    "hadrien.jean",
    "berenice.berger",
    "clarisse.da-silva",
    "adrien.schmitt",
    "anais.nicolas",
    "mia.philippe",
    "aurore.lecomte1",
    "adam.dupuis",
    "thiago.robin",
    "nora.bertrand",
    "louison.garnier",
    "auguste.leclercq",
    "mathys.renaud1",
    "leon.muller",
    "eva.lefebvre",
    "maeline.renard",
    "clara.fournier",
    "sarah.brun1",
    "maelyne.bernard",
    "lucien.gonzalez",
    "tessa.renard",
    "naomi.fontai",
    "yanis.vincent",
    "constance.boyer",
    "albane.morel",
    "ana.leroy",
    "timeo.thomas",
    "maelys.mathieu",
    "aubin.da-silva",
    "eloise.lambert",
    "aaron.renaud",
    "loic.renard",
    "aurore.carpentier",
    "aymeric.guillaume",
    "melvin.dufour",
    "claire.richard1",
    "ilyes.michel",
    "louisa.denis",
    "loane.bernard",
    "diego.michel",
    "ilan.dufour1",
    "ethan.rolland",
    "anaelle.boyer1",
    "enola.martin",
    "tony.carpentier",
    "ambre.blanchard",
    "emilie.richard",
    "leane.philippe",
    "soren.roux",
    "damien.rodriguez",
    "diane.morin",
    "tess.boyer",
    "yanis.perez",
    "manon.olivier1",
    "martin.blanc",
    "tony.bertrand",
    "zoe.roux",
    "leandre.aubert",
    "mathilde.roussel1",
    "ruben.marie",
    "dorian.garcia1",
    "timothe.lopez",
    "gauthier.gauthier",
    "jordan.rodriguez",
    "inaya.leclerc",
    "leane.muller",
    "alessio.gaillard",
    "axel.marchand1",
    "hector.robert",
    "lily.philippe",
    "nicolas.david7",
    "armand.robin",
    "maelie.dumas",
    "noelie.nicolas",
    "anthony.nguyen",
    "florian.morel",
    "come.fournier",
    "adrien.leroy",
    "kenzo.vidal",
    "constance.guillot",
    "auguste.faure",
    "remi.noel",
    "joshua.roux1",
    "victor.bernard1",
    "bastien.moulin",
    "nina.denis",
    "elias.leclerc",
    "elias.jean",
    "maely.robert",
    "charles.rodriguez",
    "lena.lemaire",
    "camille.fernandez",
    "agathe.riviere",
    "tess.lambert",
    "hanae.picard",
    "naomi.leroy",
    "margot.marie",
    "yanis.hubert",
    "florian.blanc",
    "tristan.sanchez",
    "jules.laurent",
    "angelina.morin",
    "esteban.moulin",
    "sara.leclerc",
    "louise.leclerc",
    "sara.roussel",
    "clea.meyer",
    "sasha.guerin1",
    "loan.roger",
    "maiwenn.caron",
    "antonin.renaud1",
    "lou.richard1",
    "gaspard.boyer",
    "maiwenn.bonnet",
    "alessio.carpentier",
    "elisa.bernard",
    "raphael.renard2",
    "louison.guillaume",
    "jeanne.leclercq",
    "justin.leclerc",
    "lois.dupuis",
    "basile.blanc",
    "antoine.renard2",
    "gaspard.muller",
    "elliot.fleury",
    "elias.garcia",
    "sasha.fabre",
    "remy.gautier",
    "loic.gaillard",
    "eloise.garcia",
    "lana.brun",
    "alessio.morin",
    "eloane.blanc",
    "abel.riviere",
    "hugo.joly",
    "celestine.marie",
    "ethan.giraud",
    "titouan.lecomte1",
    "fanny.durand",
    "robin.pierre",
    "andrea.david",
    "julia.menard",
    "alix.nguyen",
    "anthony.rousseau2",
    "mathieu.david",
    "eve.rousseau",
    "kenzo.jean",
    "celia.richard",
    "marceau.gonzalez",
    "joris.lefevre",
    "charly.bernard1",
    "capucine.fournier",
    "valentin.adam",
    "kiara.garnier",
    "leo.morin2",
    "ava.guillaume",
    "enzo.garnier2",
    "mael.guillaume",
    "garance.leroux",
    "giulia.dufour1",
    "melody.rey",
    "aubin.sanchez",
    "joris.sanchez",
    "florian.lefebvre1",
    "jeanne.masson",
    "aubin.denis",
    "melvin.fernandez",
    "luna.lopez",
    "helena.martin",
    "loris.leclercq",
    "julian.bertrand",
    "yanis.noel",
    "gael.renard",
    "celia.faure",
    "nino.renard",
    "kelya.dufour",
    "lohan.perrin",
    "lina.menard",
    "elia.menard",
    "valentin.colin",
    "eden.andre",
    "mathieu.guillaume",
    "tristan.fleury",
    "mael.rolland",
    "eve.denis",
    "noah.clement",
    "mae.rodriguez",
    "alice.mercier1",
    "line.arnaud",
    "eloise.blanchard",
    "celian.roger",
    "antoine.andre",
    "maelya.pierre",
    "valentina.garcia",
    "julia.hubert",
    "angele.fernandez",
    "manon.blanc1",
    "eleonore.dufour",
    "solene.rodriguez",
    "marilou.menard",
    "soren.brunet",
    "noham.renaud",
    "mael.marie",
    "emilie.francois",
    "anaelle.nguyen",
    "nino.dufour",
    "louane.mercier",
    "lilian.muller",
    "theodore.andre",
    "thomas.schmitt",
    "lylou.rousseau",
    "ava.caron",
    "tristan.adam",
    "maelys.gautier",
    "yanis.henry",
    "maeva.morel",
    "maely.bourgeois",
    "lia.david",
    "gaetan.leclerc",
    "thibaut.dufour",
    "aaron.berger",
    "lino.robin",
    "nathan.nicolas2",
    "jean.chevalier",
    "ilan.deschamps",
    "jonas.martin",
    "jade.rey",
    "damien.leroy1",
    "tessa.garcia",
    "elia.blanc",
    "claire.roger2",
    "timeo.le-gall",
    "tim.dupont",
    "corentin.bernard",
    "victor.lemaire",
    "baptiste.lefevre3",
    "berenice.rodriguez",
    "anais.lacroix1",
    "thomas.morel1",
    "noe.riviere",
    "lilly.moreau",
    "selene.fontai",
    "loan.adam",
    "david.renaud1",
    "lilian.clement",
    "ava.roy",
    "mila.lefevre",
    "pauline.petit1",
    "yanis.deschamps",
    "enora.brun",
    "lina.jean",
    "charles.dupuis",
    "oscar.leroy",
    "julian.joly",
    "victor.blanc",
    "melissa.morin1",
    "anais.bonnet",
    "joris.dubois",
    "ethan.sanchez",
    "jules.olivier",
    "maelys.schmitt",
    "maxime.lucas1",
    "giulia.francois",
    "emmie.marie",
    "victoria.roger",
    "clement.rey",
    "alexia.lefevre2",
    "lino.sanchez",
    "louis.dupont3",
    "solene.martinez",
    "oscar.giraud",
    "lya.bonnet",
    "emeline.bonnet",
    "pierre.garnier",
    "lilian.deschamps1",
    "amaury.durand",
    "lisa.picard",
    "remi.simon2",
    "clarisse.rodriguez",
    "manon.morel",
    "johan.perrin",
    "mia.durand",
    "fabien.roussel3",
    "capucine.roche",
    "tristan.morel",
    "sophia.picard",
    "mylan.martin",
    "alessio.colin",
    "stella.philippe",
    "mahe.blanchard",
    "leonard.guillaume",
    "faustine.perrin1",
    "benjamin.blanc",
    "luka.fleury",
    "lise.berger",
    "maelle.le-gall1",
    "sasha.schmitt",
    "johan.dubois",
    "ambre.roy",
    "ava.roger",
    "helena.bernard",
    "noemie.colin",
    "celian.richard1",
    "eliot.perrin",
    "alexandre.sanchez",
    "ilan.menard",
    "malone.lemaire",
    "loane.chevalier",
    "lisa.rey",
    "mya.gerard",
    "livia.marchand",
    "eliot.laurent",
    "noam.le-gall",
    "eliot.dupont",
    "noam.robin",
    "pablo.brunet",
    "juliette.clement1",
    "esteban.rousseau",
    "pablo.leroux",
    "norah.pierre",
    "matheo.duval",
    "angelina.dumont",
    "marius.giraud",
    "celestin.lacroix",
    "thiago.lemoine",
    "leane.lacroix",
    "leo.henry",
    "maiwenn.david",
    "gaetan.lemoine",
    "thiago.mathieu",
    "mathilde.leclercq",
    "mya.fabre",
    "lina.blanc",
    "julian.muller",
    "lilly.robin",
    "bastien.gerard",
    "elio.lecomte",
    "esteban.legrand",
    "lenny.blanchard",
    "nolhan.philippe",
    "kelya.francois",
    "aurelien.gauthier",
    "alexandre.bertrand",
    "adrien.gaillard",
    "anaelle.arnaud",
    "elise.morin2",
    "eve.legrand",
    "soline.nicolas",
    "julie.fontai",
    "agathe.gautier1",
    "pauline.gaillard2",
    "aubin.girard2",
    "nino.denis",
    "soline.morin",
    "fabien.schmitt",
    "anaelle.francois1",
    "julia.fontai",
    "marilou.barbier",
    "enzo.sanchez",
    "romane.aubert",
    "margaux.louis",
    "titouan.garnier",
    "rose.leroy",
    "nora.leroy",
    "matteo.meunier",
    "amandine.brunet2",
    "amaury.garcia",
    "mila.perrin",
    "abel.blanchard",
    "alessio.leroux",
    "loan.meyer",
    "lucy.blanchard",
    "valentin.robin1",
    "capucine.bourgeois",
    "timothee.lemaire",
    "armand.adam",
    "sohan.da-silva",
    "lena.leroy",
    "anais.bourgeois",
    "melody.dubois",
    "maelya.fabre",
    "elisa.guillot1",
    "lucie.guillaume",
    "pablo.laurent",
    "charles.martin",
    "elio.martinez",
    "anna.robert2",
    "jeanne.da-silva",
    "tim.schmitt",
    "livia.le-gall",
    "sohan.nguyen",
    "fabien.marie",
    "maeline.joly",
    "lucile.louis",
    "elliot.boyer",
    "lea.lefevre2",
    "ryan.martinez",
    "albane.bourgeois",
    "alois.noel",
    "maya.robin",
    "lison.meyer",
    "hadrien.rodriguez",
    "amelia.dupuis",
    "mathieu.giraud",
    "kylian.lemoine",
    "alexandra.garnier",
    "clementine.girard1",
    "auguste.dupuis",
    "daphne.renard",
    "nicolas.simon1",
    "julian.lucas",
    "erwan.durand",
    "sara.fleury",
    "elio.mercier",
    "leandre.clement",
    "leo.richard",
    "ilyes.leroux",
    "roxane.jean",
    "edouard.garcia",
    "sophie.menard1",
    "theo.pierre2",
    "hector.bonnet",
    "fabien.colin1",
    "enola.pierre",
    "bastien.fabre",
    "marie.lefevre1",
    "valentin.michel",
    "leandro.denis",
    "melina.dupont",
    "cassandre.fournier",
    "victoria.roux",
    "loane.mathieu",
    "amelia.pierre",
    "anaelle.philippe",
    "elliot.robert",
    "berenice.lemoine",
    "helena.morin1",
    "sandro.lecomte",
    "eline.renard",
    "mathias.meunier",
    "romain.perez",
    "mia.renard",
    "rafael.aubert",
    "romane.francois",
    "tess.muller",
    "angelo.simon1",
    "ilan.leclerc",
    "come.giraud",
    "aurore.perrin",
    "david.lopez2",
    "elena.da-silva",
    "alban.fournier",
    "angelina.pierre",
    "claire.marchand1",
    "giulia.robin",
    "charline.blanchard",
    "lya.morel",
    "laura.dumas1",
    "eden.rousseau",
    "nathan.rey",
    "chiara.marchand",
    "chiara.fontai",
    "eline.gaillard",
    "axelle.dupont1",
    "leo.bertrand",
    "dorian.thomas1",
    "noe.henry",
    "kenzo.dufour",
    "alban.dupuis1",
    "anaelle.roche",
    "luca.masson",
    "eloane.moreau",
    "thibault.henry2",
    "william.le-gall",
    "lois.bernard1",
    "rafael.rey",
    "charlie.colin",
    "romane.lefebvre",
    "sohan.da-silva1",
    "kenzo.gerard",
    "aaron.leclerc",
    "basile.bernard",
    "matheo.roche",
    "lilou.andre1",
    "guillaume.simon6",
    "ugo.joly",
    "nino.fournier",
    "morgan.brun",
    "malone.vincent",
    "maiwenn.martin",
    "diego.riviere",
    "jules.nicolas",
    "alyssia.menard",
    "sandro.lambert",
    "melvin.roy",
    "armand.francois",
    "maely.philippe",
    "nicolas.blanc",
    "tiago.renard",
    "mathis.roy1",
    "loic.lemaire",
    "enzo.brunet2",
    "roxane.louis",
    "matthieu.aubert",
    "rachel.giraud",
    "helena.renard",
    "lyam.legrand",
    "simon.louis",
    "enzo.lambert",
    "rafael.fleury",
    "luis.le-gall",
    "mila.andre",
    "ambre.lemoine1",
    "louane.vidal",
    "erwan.henry",
    "helena.morin2",
    "pauline.fontai",
    "soan.lefebvre",
    "elouan.andre1",
    "kais.rodriguez",
    "anna.robin",
    "benjamin.renard",
    "lyam.meyer",
    "mael.lefebvre",
    "william.mercier1",
    "martin.lefebvre",
    "flora.lucas",
    "gabin.louis",
    "margot.david",
    "lila.garnier",
    "mae.marie",
    "louisa.lefevre",
    "lise.hubert",
    "ilan.moulin1",
    "lenny.richard",
    "nathanael.bertrand",
    "soan.thomas",
    "nino.gaillard",
    "melvin.riviere",
    "leonard.moreau",
    "aurore.gautier",
    "nina.moreau",
    "tessa.roy",
    "clement.roger",
    "alois.lefevre",
    "margot.blanc",
    "nino.dumas",
    "rayan.pierre",
    "gaetan.colin",
    "juliette.philippe",
    "romain.thomas",
    "louison.dufour",
    "anaelle.blanc",
    "mya.rolland",
    "tony.arnaud",
    "melina.dubois",
    "hugo.perez",
    "sandro.leroy",
    "adam.meunier",
    "esteban.rolland",
    "hanae.adam",
    "lison.bertrand",
    "enora.fleury",
    "lison.denis2",
    "thomas.pierre",
    "timothe.robert",
    "nina.lecomte1",
    "alexandra.duval",
    "lia.martin",
    "gaetan.lemoine1",
    "naomi.bonnet1",
    "juliette.vidal",
    "ninon.brunet1",
    "claire.duval",
    "eden.renaud",
    "lilou.lopez",
    "alyssia.louis",
    "corentin.gautier",
    "gabriel.leroux",
    "emeline.garcia",
    "matheo.rey",
    "pablo.gerard",
    "hadrien.fontai",
    "alexia.michel",
    "tess.lecomte",
    "kais.meyer",
    "rafael.david",
    "ezio.marchand",
    "chiara.olivier",
    "ana.bonnet",
    "amandine.fontai",
    "garance.lacroix",
    "melissa.guerin1",
    "diane.jean",
    "tiago.garcia",
    "nathan.roussel",
    "alix.picard",
    "mya.arnaud",
    "justine.dupont1",
    "louna.clement",
    "eliot.rey",
    "fabien.roux",
    "jeanne.charles",
    "pauline.hubert",
    "rayan.dubois1",
    "soline.arnaud",
    "jeanne.robert",
    "mahe.laurent",
    "jules.picard",
    "margaux.masson",
    "eline.nicolas",
    "andrea.duval",
    "camille.fleury",
    "leane.marie",
    "tess.fernandez",
    "louisa.lefebvre",
    "laly.joly",
    "mila.simon",
    "clementine.laurent",
    "alex.morel",
    "nathan.guerin",
    "lois.lemoine",
    "noe.gaillard",
    "tom.marie2",
    "rafael.louis",
    "valentin.lecomte1",
    "ugo.lambert",
    "morgan.rousseau",
    "alexis.gonzalez",
    "charlie.fernandez1",
    "lana.gauthier",
    "maely.lopez",
    "aurore.barbier2",
    "marine.michel",
    "rachel.roger",
    "remy.muller",
    "nils.martinez",
    "capucine.robin",
    "adele.bertrand2",
    "solene.rolland",
    "valentina.gaillard",
    "rachel.sanchez",
    "lisa.roger",
    "margot.leroy",
    "ines.noel1",
    "charline.fontai1",
    "soline.simon",
    "lylou.boyer",
    "louis.louis",
    "naomi.picard",
    "louanne.menard1",
    "angelo.roger",
    "maeline.lefebvre",
    "corentin.dufour",
    "tess.lecomte1",
    "lukas.nguyen",
    "roxane.chevalier",
    "selena.guillot",
    "selena.mercier",
    "mathieu.dumas",
    "flavie.joly",
    "anais.guillaume",
    "lila.hubert",
    "selena.nicolas",
    "loris.guillaume",
    "constance.jean",
    "milo.leclercq",
    "maiwenn.blanc",
    "william.andre",
    "eleonore.lecomte",
    "louise.dupuis",
    "emmie.rodriguez",
    "rayan.colin",
    "charlie.fabre",
    "lucien.blanc",
    "elsa.chevalier",
    "roxane.noel",
    "elia.robert",
    "louison.nicolas",
    "diane.adam",
    "nina.leroux",
    "tony.meunier",
    "cassandra.roger",
    "faustine.masson",
    "elise.lemaire2",
    "rose.robert",
    "pauline.sanchez",
    "elsa.david",
    "samuel.lecomte1",
    "mathilde.colin",
    "emmy.deschamps",
    "amandine.caron",
    "emilie.picard2",
    "william.picard",
    "livio.fernandez",
    "eline.renaud",
    "livia.morel",
    "agathe.duval",
    "clementine.meunier",
    "justin.jean",
    "selena.roux",
    "titouan.riviere",
    "livio.roche",
    "ewen.lucas",
    "thais.olivier",
    "leonie.vincent",
    "clea.muller",
    "lison.giraud",
    "tess.marchand",
    "lana.bonnet",
    "selena.laurent",
    "diane.dubois",
    "sophia.dupuis",
    "elouan.deschamps",
    "eline.simon",
    "laura.legrand1",
    "celestine.morel",
    "mila.rodriguez",
    "noemie.schmitt",
    "luna.fournier",
    "leonie.rousseau",
    "apolline.rolland",
    "fabien.mathieu",
    "loane.guillot",
    "roxane.philippe",
    "maelia.muller",
    "jade.roussel",
    "anna.dumont",
    "chloe.jean1",
    "eleonore.dumas",
    "amelie.giraud",
    "lea.perrin1",
    "olivia.leroy1",
    "gauthier.duval",
    "alexia.garnier1",
    "eliot.jean",
    "alexandra.dumont",
    "celia.gautier1",
    "eva.lecomte",
    "kais.bonnet",
    "faustine.robert",
    "maelya.dupont",
    "norah.dufour",
    "ava.arnaud",
    "alyssa.muller",
    "clemence.charles",
    "clarisse.lemaire",
    "elliot.blanc",
    "teo.petit",
    "guillaume.caron3",
    "nathanael.durand",
    "amelia.louis",
    "lily.da-silva",
    "maeva.da-silva2",
    "anais.gauthier1",
    "milan.riviere",
    "meline.gauthier",
    "jonas.lecomte",
    "thiago.meunier",
    "louna.bourgeois1",
    "elya.joly",
    "marilou.duval",
    "elise.picard1",
    "antonin.masson",
    "thibaut.david",
    "selena.philippe",
    "maelyne.dupont",
    "fabio.martinez",
    "joshua.denis",
    "emmie.bertrand",
    "lana.berger",
    "ethan.guerin",
    "manon.bertrand",
    "nils.robin",
    "lilian.renaud",
    "lya.hubert",
    "ruben.dumas",
    "eleonore.blanchard",
    "loic.chevalier"
]


def reset_users():
    global USERS_STACK
    USERS_STACK = list(USERS)
    shuffle(USERS_STACK)


USERS_STACK = USERS
reset_users()


def get_random_user():
    global USERS_STACK
    if not USERS_STACK:
        reset_users()
    return USERS_STACK.pop()


def get_user_password(user: str):
    if user == 'admin':
        return 'admin'
    return 'demo'
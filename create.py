#!/usr/bin/python

import random
import string
import json

chance_unengaged = 0.1 
chance_open = 0.5
chance_click = 0.2

def echo_event(em, ev, ts):
  event_obj = {"email": em, "event": ev, "timestamp": ts}
  if (ev == "click"):
    event_obj["url"] = "http://example.com/" + ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(11))
  print json.dumps(event_obj)

def create_events(email, min, max, start, end):
  emails = random.randint(min, max)
  #print "Creating " + str(emails) + " emails for " + email

  unengaged = (random.random() < chance_unengaged)

  last_start = start
  for i in range(1, emails):
    #print "Delivered status for email " + str(i)
    last_start = random.randint(last_start, last_start + int((end-last_start)/(emails-i)))
    echo_event(email, "delivered", last_start) 
    if (not unengaged):
      for popens in range(1, 5):
        if (random.random() < chance_open):
          last_open = last_start + random.randint(60, 86400)
          echo_event(email, "open", last_open)
          for pclicks in range(1, 3):        
            if (random.random() < chance_click):
              last_click = last_open + random.randint(60, 1200)
              echo_event(email, "click", last_click)

        





def main():
  addresses = ["castaneda.higgins@ecratic.biz", "hopper.miranda@steeltab.us", "duffy.chen@kaggle.net", "bond.rollins@fanfare.io", "caldwell.welch@comcur.org", "angela.ratliff@caxt.ca", "alba.carroll@typhonica.me", "hopkins.gilmore@exoplode.name", "kathleen.cline@bugsall.com", "hensley.pratt@turnling.info", "lynn.peterson@glukgluk.co.uk", "oconnor.carson@kyaguru.tv", "deirdre.rich@boilicon.biz", "anne.george@gluid.us", "earnestine.gates@combot.net", "simpson.clark@moreganic.io", "mallory.henry@polarium.org", "bean.dorsey@golistic.ca", "conway.roy@phormula.me", "jeannette.browning@pigzart.name", "faulkner.david@xixan.com", "willa.erickson@zuvy.info", "leigh.kim@prowaste.co.uk", "wilkerson.abbott@ecrater.tv", "angie.phillips@corpulse.biz", "tanner.hull@prosely.us", "pierce.lara@microluxe.net", "aisha.drake@zenthall.io", "warner.reid@acium.org", "dianna.nielsen@signidyne.ca", "ayers.olsen@interloo.me", "carver.spencer@skybold.name", "frost.reyes@techtrix.com", "silvia.young@protodyne.info", "bianca.bray@earthmark.co.uk", "galloway.branch@ginkogene.tv", "shelby.sellers@magnemo.biz", "shawna.snow@farmage.us", "frederick.pierce@idetica.net", "cleveland.norman@vurbo.io", "booth.newton@marvane.org", "mccoy.leonard@brainclip.ca", "kellie.bell@dogspa.me", "eloise.joyner@ginkle.name", "minerva.raymond@incubus.com", "queen.velasquez@exovent.info", "cortez.moody@darwinium.co.uk", "prince.small@moltonic.tv", "thompson.aguilar@comvey.biz", "daisy.massey@vantage.us", "stanton.ayala@anarco.net", "meyer.knight@tingles.io", "ware.house@bisba.org", "helene.lancaster@springbee.ca", "joyner.stein@extragen.me", "janette.barnes@puria.name", "tracy.henderson@pyramax.com", "austin.roberson@equitax.info", "torres.riggs@codact.co.uk", "latoya.french@coriander.tv", "salazar.campbell@zytrac.biz", "lorena.hogan@indexia.us", "griffith.henson@exosis.net", "lorene.landry@naxdis.io", "fischer.ashley@signity.org", "reyna.walsh@cubicide.ca", "patel.harmon@concility.me", "jayne.nieves@quintity.name", "roth.cunningham@macronaut.com", "myrtle.oconnor@isologica.info", "rich.roth@ezentia.co.uk", "alyce.clarke@jasper.tv", "crane.bruce@assitia.biz", "joanna.wall@buzzness.us", "mcpherson.mejia@mantrix.net", "margo.gould@hawkster.io", "leah.madden@slofast.org", "paige.cotton@apextri.ca", "corinne.tyson@zisis.me", "desiree.fitzpatrick@confrenzy.name", "isabella.mckenzie@ziggles.com", "dotson.shannon@biohab.info", "joanne.lindsay@bullzone.co.uk", "ramsey.carlson@comtest.tv", "rios.craig@zytrex.biz", "shana.hess@zensus.us", "addie.conrad@interodeo.net", "marci.barrera@xyqag.io", "ashley.beck@yogasm.org", "alissa.albert@oronoko.ca", "constance.howe@eyeris.me", "randolph.vazquez@isodrive.name", "charlotte.kelley@irack.com", "peggy.vega@primordia.info", "nona.banks@interfind.co.uk", "norman.bender@ovolo.tv", "ruiz.simon@franscene.biz", "pate.dickson@imkan.us", "michael.larsen@ultrasure.net", "petra.nixon@kraggle.io", "gonzales.adkins@tsunamia.co.uk", "cantrell.good@centuria.com", "burke.juarez@cormoran.us", "joyce.kaufman@orbalix.me", "schneider.brown@rugstars.org", "melendez.rivers@insuresys.net", "crystal.justice@lumbrex.biz", "annie.mccarty@ultrimax.ca", "eleanor.klein@realmo.name", "milagros.manning@canopoly.tv", "madeline.herring@daido.io", "susanna.travis@housedown.info", "henderson.gomez@ronbert.co.uk", "lori.vincent@supportal.com", "herman.strong@quarx.us", "edna.merritt@anacho.me", "isabel.chan@zaj.org", "iva.figueroa@lyrichord.net", "simmons.bridges@namebox.biz", "franks.frye@imkan.ca", "buck.jacobs@cablam.name", "stefanie.cummings@neocent.tv", "katheryn.graham@voipa.io", "melton.salazar@exoblue.info", "mercer.harris@spacewax.co.uk", "olsen.gay@zappix.com", "laverne.english@kidstock.us", "kendra.lindsey@apextri.me", "gregory.leon@exoplode.org", "alston.silva@ebidco.net", "florence.smith@geekular.biz", "brewer.benton@oatfarm.ca", "delacruz.horton@uncorp.name", "barnett.wynn@menbrain.tv", "renee.holcomb@orbaxter.io", "bradshaw.warren@signity.info", "cathryn.mercer@zentime.co.uk", "adela.shepard@endipin.com", "janine.randolph@zillacon.us", "fulton.sykes@zedalis.me", "martin.meyers@gorganic.org", "beard.barber@hivedom.net", "santana.blake@temorak.biz", "heather.mcmillan@noralex.ca", "julia.pruitt@pheast.name", "herminia.bradley@automon.tv", "berta.welch@optyk.io", "chaney.stout@marqet.info", "simon.walker@izzby.co.uk", "billie.buck@medmex.com", "teri.schwartz@ceprene.us", "jayne.rose@exoswitch.me", "gena.farrell@plutorque.org", "janis.wood@geekosis.net", "toni.russell@solaren.biz", "hanson.herman@rubadub.ca", "doreen.mckenzie@accidency.name", "selena.moses@interfind.tv", "angelique.jenkins@aquafire.io", "gonzalez.schmidt@urbanshee.info", "lilian.tyler@zorromop.co.uk", "cheri.gilmore@zialactic.com", "julie.carney@xixan.us", "parks.garza@digigene.me", "tabitha.frost@candecor.org", "morales.hewitt@flexigen.net", "compton.clemons@verbus.biz", "candy.newton@accuprint.ca", "kristina.pacheco@anivet.name", "madeleine.monroe@softmicro.tv", "tiffany.middleton@mangelica.io", "burt.baxter@opportech.info", "jasmine.morton@sureplex.co.uk", "moran.kennedy@aquoavo.com", "good.key@zentility.us", "cherry.hughes@slambda.me", "hickman.curtis@wazzu.org", "debra.rutledge@snacktion.net", "rebecca.morrison@earbang.biz", "gutierrez.burt@eschoir.ca", "solis.small@caxt.name", "ines.gentry@telpod.tv", "gilliam.macias@assistix.io", "terra.miller@concility.info", "leigh.gonzales@strezzo.co.uk", "cheryl.duncan@puria.com", "brennan.armstrong@myopium.us", "staci.acosta@cinaster.me", "kim.padilla@zillanet.org", "miranda.dawson@nurplex.net", "ross.merrill@daycore.biz", "elisa.odom@medesign.ca", "stephenson.pierce@quizmo.name", "guerra.stokes@synkgen.tv", "deloris.floyd@comverges.io", "nichols.farmer@roboid.info", "gillespie.solis@trollery.co.uk", "hendrix.ratliff@niquent.com", "tania.walsh@fitcore.us", "minerva.espinoza@koogle.me"]
  for address in addresses:
    create_events(address, 6, 52, 1422400000, 1451200000)





if __name__ == "__main__":
  main()

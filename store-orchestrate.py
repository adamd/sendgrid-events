#!/usr/bin/python

import os, sys, json, porc

def process_event(js, c):
  event_types = ["delivered", "click", "open"]
  if (js["event"] in event_types):
    print js
    # First try a patch (will fail if new email address)
    njs = {"email": js["email"]}
    njs[js["event"] + "_timestamp"] = js["timestamp"]
    r = c.patch_merge("engagements", js["email"], njs)

    # Initialize engagements object for this email address
    if (r.status_code == 404):
      # Initialize other event types
      for etp in event_types:
        if (js["event"] != etp):
          njs[etp + "_timestamp"] = 0
      # Add timestamp from current event
      njs["first_timestamp"] = js["timestamp"]
      c.put("engagements", js["email"], njs)
    
    

# import_event expects:
# js - JSON object created from single SendGrid event
# c - Orchestrate client object
# Adds a new item to raw_events with an auto-generated key
# Only accepts events as declared in event_types
def import_event(js, c):
  event_types = ["delivered", "click", "open"]
  if (js["event"] in event_types):
    print js
    c.post("raw_events", js)

# import_file expects:
# fn - filename containing one SendGrid event JSON per line
# tp (optional) - type of event import, defaults to raw 
# Only use this function for testing. If you want to use this to store live events into Orchestrate
# incorporate the process_event or import_event function into your project
def import_file(fn, tp):
  print "importing from " + fn

  c = porc.Client(os.environ['OIO_SGEVENTS'])
  f = open(fn)
  for line in f:
    js = json.loads(line)
    if (tp == "raw" or tp == None):
      import_event(js, c)
    elif (tp == "process"):
      process_event(js, c)
  f.close

if __name__ == "__main__":
  if (len(sys.argv) > 1):
    import_type = "raw"
    if (len(sys.argv) > 2): import_type = sys.argv[2]
    import_file(sys.argv[1], import_type)
  else:
    print "Expect file as argument"


import csv
f = open("basictext", "w")
s = open("sampleset.csv", "r")
doc = csv.DictReader(s)

def add_heading(tag, start = False):
  if not start:
    f.write("\n  </div>\n</div>\n")
  f.write("<h4><a href='{0}'></a>{1}</h4>\n".format(tag, tag.capitalize()))
  f.write('<div class="container">\n  <div class="row">\n')

heading = ""
idx = 0

for item in doc:
  if item['tag'] != heading:
    start = False
    if heading == "":
      start = True
    heading = item['tag']
    idx = 0
    add_heading(heading, start)
  elif not idx % 4:
    f.write("  </div>\n  <div class='row'>\n")
  idx += 1
  f.write('<div class="col-md-3"><a href="{0}"><img src="{1}"/></a></div>'.format(item['url'], item['Large Square']))

f.write("\n  </div>\n</div>\n")

f.close()
s.close()

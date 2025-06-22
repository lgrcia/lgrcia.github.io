#import "@preview/cmarker:0.1.6"

#set text(font: "Arial")
#show heading.where(level: 1): set text(size: 22pt)
#set text(size: 10.5pt)
#show link: set text(rgb(53, 116, 234))
#let gray(str) = text(rgb(120, 120, 120), str)
#set par(leading: 0.8em)

#let data = json("data/resume.json")
#let contact = json("data/contact.json")

#let render_item(item) = {
  // Convert Markdown to Typst using the built-in markdown function
  cmarker.render(item)
}

= #data.name
#text(size: 13pt, gray(data.summary))
#v(-6pt)
#link("mailto:" + contact.mail) | #link(contact.github)[github.com/lgrcia] | #link(contact.linkedin)[linkedin]

#block(inset: 10pt, for stat in data.stats {
  list.item(render_item(stat))
})

== Experience

#block(inset: 10pt, for job in data.experience {
  strong(job.title) + "  " + gray(render_item(job.location))
  for item in job.description { list.item(render_item(item)) }
  v(4pt)
})

== Education

#block(inset: 10pt, for edu in data.education {
  strong(edu.degree) + ", " + gray(edu.location) + "\n"
})

# Inspiration

Cobratate borrows its vocabulary from the public persona of Andrew Tate. It does not borrow his businesses, his legal position, or his views. The project is an esoteric language written during a hackathon, and it is not affiliated with him.

## The person

Emory Andrew Tate III was born on 1 December 1986 in Washington, D.C. He is a British-American former professional kickboxer and a media personality, also known publicly as Cobra Tate and as Top G. He came to wider attention in 2016 on the British edition of the reality series *Big Brother*, and later built a large online audience around displays of wealth, physical training, and a self-described rejection of ordinary employment, which he and his audience often call the Matrix.

Phrases from that public style are the source of the keywords. "What color is your Bugatti?" became the print statement. The Matrix became the program banners and the name of input. Cobra and Tate became the language's name. Hustle became the word for a function. Top G is the prompt of the read-eval-print loop. Sigma and beta are wider internet slang from the same milieu, used here only as the two booleans.

The kickboxing nickname and the online nickname are why the language is called Cobratate rather than, for example, a neutral diminutive. The file extension `.cbt` is an abbreviation of that name. None of this is a claim that Tate designed, approved, or knows of the language.

## What the language does with those words

The design rule, fixed on the night the interpreter was first written, is that the joke stops at the token. `WHAT COLOR IS YOUR BUGATTI` prints. `GRIND WHILE` is a while-loop. `HUSTLE` is a function. `CASH OUT` returns. A reader who knows the persona can hear the monologue. A reader who does not can still use the reference manual, because each phrase has one meaning and the meanings compose in the ordinary way.

The sample program `examples/intro/fizz.cbt` is the clearest illustration. Multiples of 3 print `COBRA`, multiples of 5 print `TATE`, and multiples of 15 print `COBRATATE`. The control flow is FizzBuzz.

## Allegations, stated as allegations

Tate is a controversial public figure, and any manual that names him has to say why the name is contested.

He and his brother Tristan Tate have been the subject of criminal investigations and charges in Romania, the United Kingdom, and the United States. Reported allegations include rape, human trafficking, assault, and offences related to sexual images. In 2026, reporting described a United Kingdom extradition request and continued Romanian proceedings. The brothers have denied the allegations. These are charges and investigations, not findings recorded by this project, and this manual does not treat them as proved.

Separate civil proceedings in the United Kingdom have concerned tax. A 2024 magistrates' court ruling on frozen funds was reported as a finding that tax had not been paid on online revenue. That is a civil matter, distinct from the criminal cases.

Tate's public statements about women have been widely criticised as misogynistic, and platforms have at times restricted his accounts on that ground. The language does not encode those statements. There is no keyword whose meaning is a claim about women, and the documentation is not a vehicle for them.

## What was deliberately left out

The evaluator has no opinion about wealth, status, or the person. Error text uses the register of the language ("not in the garage", "beta behavior") because a diagnostic is part of the surface. The reference manual uses ordinary technical English. Contributors should keep that split: persona in the tokens, rules in the manual.

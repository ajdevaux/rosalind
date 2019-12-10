"""
I wrote this is such a way that I, as a biology major, could understand it,
rather that as a CS or stats major. Clearly there are more efficient ways to do this.
"""

def mendel(pop):
    """
    TT=dominant homozygous
    Tt=heterozygous
    tt=recessive homozygous
    """
    dom, het, rec = pop
    total = sum(pop)

    TTxTT =  (dom/total) * ((dom-1)/(total-1))
    TTxTt =  (dom/total) * ((het)/(total-1))
    TTxtt =  (dom/total) * ((rec)/(total-1))

    TtxTT = (het/total) * ((dom)/(total-1))
    TtxTt = (het/total) * ((het-1)/(total-1))
    Ttxtt = (het/total) * ((rec)/(total-1))

    ttxTT = (rec/total) * ((dom)/(total-1))
    ttxTt = (rec/total) * ((het)/(total-1))
    ttxtt = (rec/total) * ((rec-1)/(total-1))

    odds_of_dom = ((TTxTT + TTxTt + TTxtt)
                  + (TTxTt + 0.75*TtxTt + 0.5*Ttxtt)
                  + (ttxTT + 0.5*ttxTt + 0*ttxtt)
    )

    return round(odds_of_dom,5)

#Deck.py

from distutils.sysconfig import customize_compiler


Card = {}
#== Major Arcana
Card[0] = ["The Fool", "The Fool is beginning a journey... \n*New Beginnings *Naivety *Leap of Faith *Adventure *Fresh Starts *Free Spirit"]
Card[1] = ["The Magician", "The Magician has a bag of tricks... \n*Manifestation *Planning *Mastery *New Skills"]
Card[2] = ["The High Priestess", "The High Priestess stands before you...  \n*Intuition *Inner Knowledge *Arcane Secrets *Advice"]
Card[3] = ["The Empress", "The Empress provides...  \n*Abundance *Love *Fortune *Success"]
Card[4] = ["The Emperor", "The Emperor commands...  \n*Loyalty *Structure *Authority *Progress"]
Card[5] = ["The Hierophant", "The Hierophant worships...  \n*Spiritual Attunement *Being at Peace *Growth"]
Card[6] = ["The Lovers", "The Lovers cherish...  \n*Relationships *Trust *Commitment *Sharing"]
Card[7] = ["The Chariot", "The Chariot pursues...  \n*Travel *Direction *Willpower"]
Card[8] = ["Strength", "Strength carries with it...  \n*Confidence *Courage *Health *Energy"]
Card[9] = ["The Hermit", "The Hermit considers these... \n *Inner Peace *Meditation *Patience *Withdrawal"]
Card[10] = ["Wheel of Fortune", "The Wheel of Fortune lifts...  \n*Change *Luck *Improvements *Going Up"]
Card[11] = ["Justice", "Justice creates...  *Accountability \n*Agreements *Truth *The Law"]
Card[12] = ["The Hanged Man", "The Hanged Man asks about...  \n*Delays *Surrender *Letting Go *Sacrifice "]
Card[13] = ["Death", "Death takes its toll...  \n*Finality *Loss *The End of a Phase *Transformation"]
Card[14] = ["Temperance", "Temperance seeks to remind us of...  \n*Balance *Compromise *Forgiveness *Cooperation"]
Card[15] = ["The Devil", "The Devil binds with...  \n*Addiction *Unhealthy Attachments *Negative Thinking"]
Card[16] = ["The Tower", "The Tower crumbles because of...  \n*Changing Foundations *Missing Support *Shock *New Projects"]
Card[17] = ["The Star", "The Star guides us to...  \n*Hope *Faith *Trust *Peace"]
Card[18] = ["The Moon", "The Moon casts...  \n*Magic *Secrets *The Arcane *Instinct"]
Card[19] = ["The Sun", "The Sun develops...  \n*Success *Vitality *Warmth *Creativity"]
Card[20] = ["Judgement", "Judgement results in...  \n*Reconciliation *Decisions *Arbitration *Intervention"]
Card[21] = ["The World", "The World has to offer...  \n*New Oppurtunities *Achievement *Fulfillment *Good Outcomes"]

#== Minor Arcana
wands = "The Wands suit represents ideas, thoughts, and the development of plans. "
cups = "The suit of Cups represents emotions, relationships, and family. "
swords = "Swords are the suit of action, achievement, and progress. "
pentacles = "The suit of Pentacles are the material world, finances, and security. "
ace = "\nThe Ace is raw power. "
two = "\nThe Two is partnership. "
three = "\nThe Three is a group. "
four = "\nThe Four is stability. "
five = "\nThe Five is unstable progress. "
six = "\nThe Six is balanced success. "
seven = "\nThe Seven is high order confusion. "
eight = "\nThe Eight is a well developed forming. "
nine =  "\nThe Nine is chaos. "
ten = "\nThe Ten shows Total Development. "
page = "\nThe Page is a person who is just starting their journey. "
knight ="\nThe Knight is a person who knows what they are doing and is reliable. "
queen = "\nThe Queen is someone who stands out and has mastery. "
king = "\nThe King has experience and possesses dominion. "

#== Suit of Wands
Card[22] = ["Ace of Wands", f"{wands} {ace}"]
Card[23] = ["Two of Wands", f"{wands} {two}"]
Card[24] = ["Three of Wands", f"{wands} {three}"]
Card[25] = ["Four of Wands", f"{wands} {four}"]
Card[26] = ["Five of Wands", f"{wands} {five}"]
Card[27] = ["Six of Wands", f"{wands} {six}"]
Card[28] = ["Seven of Wands", f"{wands} {seven}"]
Card[29] = ["Eight of Wands", f"{wands} {eight}"]
Card[30] = ["Nine of Wands", f"{wands} {nine}"]
Card[31] = ["Ten of Wands", f"{wands} {ten}"]
Card[32] = ["Page of Wands", f"{wands} {page}"]
Card[33] = ["Knight of Wands", f"{wands} {knight}"]
Card[34] = ["Queen of Wands", f"{wands} {queen}"]
Card[35] = ["King of Wands", f"{wands} {king}"]

#== Suit of Cups
Card[36] = ["Ace of Cups", f"{cups} {ace}"]
Card[37] = ["Two of Cups", f"{cups} {two}"]
Card[38] = ["Three of Cups", f"{cups} {three}"]
Card[39] = ["Four of Cups", f"{cups} {four}"]
Card[40] = ["Five of Cups", f"{cups} {five}"]
Card[41] = ["Six of Cups", f"{cups} {six}"]
Card[42] = ["Seven of Cups", f"{cups} {seven}"]
Card[43] = ["Eight of Cups", f"{cups} {eight}"]
Card[44] = ["Nine of Cups", f"{cups} {nine}"]
Card[45] = ["Ten of Cups", f"{cups} {ten}"]
Card[46] = ["Page of Cups", f"{cups} {page}"]
Card[47] = ["Knight of Cups", f"{cups} {knight}"]
Card[48] = ["Queen of Cups", f"{cups} {queen}"]
Card[49] = ["King of Cups", f"{cups} {king}"]


#== Suit of Swords
Card[50] = ["Ace of Swords", f"{swords} {ace}"]
Card[51] = ["Two of Swords", f"{swords} {two}"]
Card[52] = ["Three of Swords", f"{swords} {three}"]
Card[53] = ["Four of Swords", f"{swords} {four}"]
Card[54] = ["Five of Swords", f"{swords} {five}"]
Card[55] = ["Six of Swords", f"{swords} {six}"]
Card[56] = ["Seven of Swords", f"{swords} {seven}"]
Card[57] = ["Eight of Swords", f"{swords} {eight}"]
Card[58] = ["Nine of Swords", f"{swords} {nine}"]
Card[59] = ["Ten of Swords", f"{swords} {ten}"]
Card[60] = ["Page of Swords", f"{swords} {page}"]
Card[61] = ["Knight of Swords", f"{swords} {knight}"]
Card[62] = ["Queen of Swords", f"{swords} {queen}"]
Card[63] = ["King of Swords", f"{swords} {king}"]


#== Suit of Pentacles
Card[64] = ["Ace of Pentacles", f"{pentacles} {ace}"]
Card[65] = ["Two of Pentacles", f"{pentacles} {two}"]
Card[66] = ["Three of Pantacles", f"{pentacles} {three}"]
Card[67] = ["Four of Pentacles", f"{pentacles} {four}"]
Card[68] = ["Five of Pentacles", f"{pentacles} {five}"]
Card[69] = ["Six of Pentacles", f"{pentacles}{six}"]
Card[70] = ["Seven of Pentacles", f"{pentacles} {seven}"]
Card[71] = ["Eight of Pentacles", f"{pentacles} {eight}"]
Card[72] = ["Nine of Pentacles", f"{pentacles} {nine}"]
Card[73] = ["Ten of Pentacles", f"{pentacles} {ten}"]
Card[74] = ["Page of Pentacles", f"{pentacles} {page}"]
Card[75] = ["Knight of Pentacles", f"{pentacles} {knight}"]
Card[76] = ["Queen of Pentacles", f"{pentacles} {queen}"]
Card[77] = ["King of Pentacles", f"{pentacles} {king}"]

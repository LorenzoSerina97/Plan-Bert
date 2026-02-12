from tokenizers import Tokenizer
from tokenizers.models import WordLevel # type: ignore
from tokenizers.trainers import WordPieceTrainer, BpeTrainer, WordLevelTrainer # type: ignore
from tokenizers.pre_tokenizers import WhitespaceSplit, Split # type: ignore
from tokenizers.processors import TemplateProcessing
from tokenizers.normalizers import Lowercase # type: ignore
import pickle
from plan import *
from transformers import PreTrainedTokenizerFast # type: ignore


tokenizer = Tokenizer(WordLevel(unk_token="[UNK]")) # type: ignore
trainer = WordLevelTrainer(special_tokens=["[UNK]", "[CLS]", "[SEP]", "[PAD]", "[MASK]", "[A]", "[SI]", "[SG]"]) # type: ignore
tokenizer.normalizer = Lowercase() # type: ignore
#Split on whitespace and newlines
tokenizer.pre_tokenizer = WhitespaceSplit() # type: ignore

with open('data/multidomain/plans', 'rb') as f:
    satellite_plans=pickle.load(f)
piani=[]
for p in satellite_plans:
    azioni=[a.name.lower().strip() for a in p.actions]
    initial_state=[a.lower().strip() for a in p.initial_state]
    goal=[a.lower().strip() for a in p.goals]
    piano="[SI] "+ " ".join(initial_state) + " [SG] " + " ".join(goal) + " [A] " + " ".join(azioni)
    piani.append(piano)
print(piani[0])
#files = ["data/dataset/logistics/train.txt","data/dataset/logistics/test.txt"]
tokenizer.train_from_iterator(piani, trainer=trainer) # type: ignore
tokenizer.post_processor = TemplateProcessing(
    single="[CLS] $A [SEP]",
    pair="[CLS] $A [SEP] $B:1 [SEP]:1",
    special_tokens=[
        ("[CLS]", tokenizer.token_to_id("[CLS]")),
        ("[SEP]", tokenizer.token_to_id("[SEP]")),
    ],
) # type: ignore
#tokenizer.save("/root/data/PlanBert/architecture/tokenizer.json")

#new_tokenizer = Tokenizer.from_file("/root/data/PlanBert/architecture/tokenizer.json")
tokenizer = PreTrainedTokenizerFast(
    tokenizer_object=tokenizer,
    model_max_length=512,
    truncation=True,
    padding="max_length",
    #tokenizer_file="/root/data/PlanBert/architecture/tokenizer.json", # You can load from the tokenizer file, alternatively
    unk_token="[UNK]",
    pad_token="[PAD]",
    cls_token="[CLS]",
    sep_token="[SEP]",
    mask_token="[MASK]",
    action_token="[A]",
    init_token="[SI]",
    goal_token="[SG]",
    
    # special_tokens=[
    #     ("[A]", tokenizer.token_to_id("[A]")),
    #     ("[SI]", tokenizer.token_to_id("[SI]")),
    #     ("[SG]", tokenizer.token_to_id("[SG]")),
    # ],

)
tokenizer.save_pretrained("architecture/multidomain/tokenizer/")
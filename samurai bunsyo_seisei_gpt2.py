from transformers import T5Tokenizer,AutoModelForCausalLM
tokenizer = T5Tokenizer.from_pretrained("rinna/japanese-gpt2-small")
model = AutoModelForCausalLM.from_pretrained("rinna/japanese-gpt2-small")

from transformers import T5Tokenizer,AutoModelForCausalLM
tokenizer = T5Tokenizer.from_pretrained("rinna/japanese-gpt2-small")
model = AutoModelForCausalLM.from_pretrained("rinna/japanese-gpt2-small")

input = tokenizer.encode("自然言語処理とは,", return_tensors="pt")

# inference
output = model.generate(input, do_sample=True, max_length=30, num_return_sequences=3)

# inferred output
print(tokenizer.batch_decode(output))

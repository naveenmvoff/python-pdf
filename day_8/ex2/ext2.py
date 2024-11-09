# Create a new text file and write some content into it.

newfile = 'ex2text.txt'

with open(newfile, 'w') as file:
    file.write("Lorem ipsum dolor sit amet consectetur adipisicing elit. Quas eveniet perspiciatis explicabo ullam est eius pariatur id adipisci reiciendis ipsa officiis sunt quis qui doloremque maiores doloribus beatae delectus, placeat dolore culpa? Obcaecati itaque provident praesentium ducimus dignissimos voluptatibus quaerat, eos asperiores neque voluptates autem, libero molestias suscipit non nam tenetur sequi est pariatur! Exercitationem repellat distinctio quod illum nihil quisquam blanditiis facilis obcaecati pariatur tempore. Commodi corporis eligendi ipsam, inventore illum repellat iusto optio magnam sapiente itaque deleniti exercitationem soluta in sed dolores dicta autem facilis non excepturi laborum explicabo placeat. Quibusdam dicta adipisci ad minima repellendus corporis necessitatibus.")
    
print(newfile)
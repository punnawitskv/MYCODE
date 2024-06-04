let width = 5

for (let i = 1; i <= width; i++)
{
    let pira = '';
    for (let j = 0; j < width - i; j++)
    {
        pira += ' '
    }
    
    for (let j = 0; j < (i*2) -1; j++)
    {
        pira += 'O'
    }
    console.log(pira)
}

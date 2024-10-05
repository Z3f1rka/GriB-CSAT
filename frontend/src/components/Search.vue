<template>
    <span class="input text-center my-10 border shadow-sm border-slate-300 placeholder-slate-400 focus:outline-none focus:border-sky-500 focus:ring-sky-500  w-full rounded sm:text-sm focus:ring-1 relative">
            <div class="grid grid-rows-1 grid-cols-12">
                <div class="grid text-left col-span-11 mx-5">
                        <input class="outline-none p-0" style="background: #E5E5E5; resize: vertical;" placeholder="Поиск " />
                </div>
                <div class="grid text-right">
                    <img src="/search.png" class="icon text-align-right self-center">
                </div>
            </div>
        </span>
</template>
<style scoped>
.line::after {
    content: '';
    width: 90%;
    height: 1px;
    background-color: black;
    display: inline-flex;
}
span:focus-within{
    border: 1px solid #4e525b79;
}
.icon {
    position: relative;
    height: 40%;
}
.focus\:border-sky-500:focus {
    --tw-border-opacity: 0.5;
    border-color: rgb(78 82 91 / var(--tw-border-opacity)) /* #0ea5e9 */;
} 
.focus\:ring-sky-500:focus {
    --tw-ring-opacity: 0.5;
    --tw-ring-color: rgb(78 82 91 / var(--tw-ring-opacity)) /* #0ea5e9 */;
}
.input {
  display: block;
  width: 20cm;
  margin: 20px auto;
  padding-left: 2%;
  background: #E5E5E5;
  background-size: 15px 15px;
  font-size: 26px;
  border: none;
  box-shadow: rgba(50, 50, 93, 0.25) 0px 2px 5px -1px,
    rgba(0, 0, 0, 0.3) 0px 1px 3px -1px;
}
</style>
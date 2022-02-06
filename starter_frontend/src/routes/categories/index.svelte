<script>

    let query = `{
allProductCategories{
    edges{
      node{
        name,
        description
      }
    }
  }
}`

    const promise = fetch('http:127.0.0.1:8000/api/', {method: 'POST', body: {query: query}})
    .then(res => {
        if (res.status != 200) {
        throw new Error(`expected status 200, got ${res.status}`)
        }

    return res.json()  
    })

    // const categories = [
    //     {
    //         name:'office essentials',
    //         description: 'all of your office essentials under one roof',
    //         image: 'https://tailwindui.com/img/ecommerce-images/home-page-02-edition-01.jpg',
    //     },
    //     {
    //         name: 'home essentials',
    //         description: 'all of your home essentials under one roof',
    //         image: 'https://tailwindui.com/img/ecommerce-images/home-page-02-edition-02.jpg',
    //     },
    //     {
    //         name: 'personal care',
    //         description: 'all of your personal care under one roof',
    //         image: 'https://tailwindui.com/img/ecommerce-images/home-page-02-edition-03.jpg',
    //     },
    //     {
    //         name: 'beauty',
    //         description: 'all of your beauty under one roof',
    //         image: 'https://images.unsplash.com/photo-1643763140886-9629048efa11?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=928&q=80',
    //     },
    //     {
    //         name: 'electronics',
    //         description: 'all of your electronics under one roof',
    //         image: 'https://images.unsplash.com/photo-1643779374792-ef7c60c75b6b?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1740&q=80',
    //     },
    //     {
    //         name: 'grocery',
    //         description: 'all of your grocery under one roof',
    //         image: 'https://images.unsplash.com/photo-1640622300363-4f295638be2e?ixlib=rb-1.2.1&ixid=MnwxMjA3fDF8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1744&q=80',
    //     },
    //     {
    //         name: 'furniture',
    //         description: 'all of your furniture under one roof',
    //         image: 'https://images.unsplash.com/photo-1643816185351-d26268eb49ef?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80',
    //     },
    //     {
    //         name: 'home decor',
    //         description: 'all of your home decor under one roof',
    //         image: 'https://images.unsplash.com/photo-1643821952224-99d425c148a6?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=688&q=80',
    //     },
    //     {
    //         name: 'kitchen',
    //         description: 'all of your kitchen under one roof',
    //         image: 'https://images.unsplash.com/photo-1643821042671-80282f7803a9?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1345&q=80',
    //     },
    //     {
    //         name: 'toys',
    //         description: 'all of your toys under one roof',
    //         image: 'https://images.unsplash.com/photo-1643819131797-46919f3009f7?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=8',
    //     }
    // ]
</script>

<div class="bg-gray-100">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="max-w-2xl mx-auto py-16 sm:py-24 lg:py-32 lg:max-w-none">
        <h2 class="text-2xl font-extrabold text-gray-900">Collections</h2>
  
        <div class="mt-6 space-y-12 lg:space-y-0 lg:grid lg:grid-cols-3 lg:gap-x-6">

            {#await promise}
                loading categories
            {:then result} 
            <pre>{result}</pre>
                
                <!-- {#each result.data as category}
                    <div class="group relative">
                        <div class="relative w-full h-80 bg-white rounded-lg overflow-hidden group-hover:opacity-75 sm:aspect-w-2 sm:aspect-h-1 sm:h-64 lg:aspect-w-1 lg:aspect-h-1">
                        <img src="{category.image}" alt="Desk with leather desk pad, walnut desk organizer, wireless keyboard and mouse, and porcelain mug." class="w-full h-full object-center object-cover">
                        </div>
                        <h3 class="mt-6 text-sm text-gray-500">
                        <a href="#">
                            <span class="absolute inset-0"></span>
                            {category.name}
                        </a>
                        </h3>
                        <p class="text-base font-semibold text-gray-900">{category.description}</p>
                    </div>
                {/each} -->

                {:catch error}
    <li>Error loading articles: {error}</li>
            {/await}

  
        </div>
      </div>
    </div>
  </div>

<div class="bg-white">
    <div class="max-w-2xl mx-auto py-16 px-4 sm:py-24 sm:px-6 lg:max-w-7xl">
      <div class="relative rounded-lg overflow-hidden lg:h-96">
        <div class="absolute inset-0">
          <img src="https://tailwindui.com/img/ecommerce-images/category-page-01-featured-collection.jpg" alt="" class="w-full h-full object-center object-cover">
        </div>
        <div aria-hidden="true" class="relative w-full h-96 lg:hidden"></div>
        <div aria-hidden="true" class="relative w-full h-32 lg:hidden"></div>
        <div class="absolute inset-x-0 bottom-0 bg-black bg-opacity-75 p-6 rounded-bl-lg rounded-br-lg backdrop-filter backdrop-blur sm:flex sm:items-center sm:justify-between lg:inset-y-0 lg:inset-x-auto lg:w-96 lg:rounded-tl-lg lg:rounded-br-none lg:flex-col lg:items-start">
          <div>
            <h2 class="text-xl font-bold text-white">Workspace Collection</h2>
            <p class="mt-1 text-sm text-gray-300">Upgrade your desk with objects that keep you organized and clear-minded.</p>
          </div>
          <a href="#" class="mt-6 flex-shrink-0 flex bg-white bg-opacity-0 py-3 px-4 border border-white border-opacity-25 rounded-md items-center justify-center text-base font-medium text-white hover:bg-opacity-10 sm:mt-0 sm:ml-8 lg:ml-0 lg:w-full">View the collection</a>
        </div>
      </div>
    </div>
  </div>
  
  
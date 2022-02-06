<script>
    import LoginForm from '$lib/components/auth/LoginForm.svelte';
    import {onMount} from 'svelte'
    import {goto} from '$app/navigation'
    import {browser} from '$app/env'
    import {isAuthenticated} from '$lib/stores/auth'

    export let redirect = '/'

    function redirectIfAuthenticated(){
        if(browser){
            if ($isAuthenticated) {
                goto(redirect)
            }
        }
    }

    onMount(() => {
        redirectIfAuthenticated()
    })
</script>

<main>
    <section class="h-screen flex items-center justify-center">
        <div class="left-side flex-1 h-screen overflow-hidden">
            <img class="object-cover h-full" src="/images/auth-bg.jpeg" alt="">
        </div>
        <div class="right-side flex-1">
            <LoginForm />
        </div>
    </section>
</main>

<style>
    .left-side{
        clip-path: polygon(0 0, 100% 0, 75% 100%, 0% 100%);
    }
</style>


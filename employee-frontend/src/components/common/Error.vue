<template>
    <p class="error-message">
        ❗{{ message }}
    </p>
</template>

<script>
export default {
    name: 'Error',
    props: {
        message: String
    }
}
</script>

<style scoped>
    .error-message {
        color: #d33c40;
    }
</style>

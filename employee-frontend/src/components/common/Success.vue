<template>
    <p class="success-message">
        ✅ {{ message }}
    </p>
</template>

<script>
export default {
    name: 'Success',
    props: {
        message: String
    }
}
</script>

<style scoped>
    .success-message {
        color: #32a95d;
    }
</style>

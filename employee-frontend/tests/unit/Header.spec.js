import { shallowMount } from '@vue/test-utils'
import Header from '@/components/common/Header.vue'

describe('Header Test', () => {
    it('renders header with correct content when created', () => {
        const wrapper = shallowMount(Header, {
            propsData: {
                title: 'Add Invoice'
            }
        })

        expect(wrapper.text()).toMatch('Add Invoice')
    })
})

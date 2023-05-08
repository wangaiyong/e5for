# 需要导入模块: from marionette_driver import Wait [as 别名]
# 或者: from marionette_driver.Wait import until [as 别名]
    def deactivate_autoplay(self):
        """
        Attempt to turn off autoplay. Return True if successful.
        """
        element_id = 'autoplay-checkbox'
        mn = self.marionette
        wait = Wait(mn, timeout=10)

        def get_status(el):
            script = 'return arguments[0].wrappedJSObject.checked'
            return mn.execute_script(script, script_args=[el])

        try:
            with mn.using_context('content'):
                # the width, height of the element are 0, so it's not visible
                wait.until(expected.element_present(By.ID, element_id))
                checkbox = mn.find_element(By.ID, element_id)

                # Note: in some videos, due to late-loading of sidebar ads, the
                # button is rerendered after sidebar ads appear & the autoplay
                # pref resets to "on". In other words, if you click too early,
                # the pref might get reset moments later.
                sleep(1)
                if get_status(checkbox):
                    mn.execute_script('return arguments[0].'
                                      'wrappedJSObject.click()',
                                      script_args=[checkbox])
                    self.marionette.log('Toggled autoplay.')
                autoplay = get_status(checkbox)
                self.marionette.log('Autoplay is %s' % autoplay)
                return (autoplay is not None) and (not autoplay)
        except (NoSuchElementException, TimeoutException):
            return False

import React from 'react'
import { CustomLink } from './CustomLink'

function NavBar (){
        return (
            <>
            <header>
                <CustomLink to="/events">События</CustomLink>
                <CustomLink to="/schedule">Расписание</CustomLink>
                <CustomLink to="/students">Студенты</CustomLink>
                <CustomLink to="/auth">Выход</CustomLink>
            </header>
            </>
        )
    }
export default NavBar
import { useRef, useEffect } from 'react'
import { useWindowSize } from 'hooks'

import './Logo.scss'

const Logo = () => {
  const ref = useRef<HTMLSpanElement[]>(null)
  const { w, h } = useWindowSize()
  
  useEffect(() => {
    const handleFocus = (e: FocusEvent) => {
      const target = e.target as HTMLElement
      if (!target) return 
      try {
        const { left, top, width, height } = target.getBoundingClientRect()
        
        const x = (left + width / 2) / w
        const y = (top + height / 2) / h
        
        const percentPos = (p: number, v: number) => p / v
        
        ref.current?.forEach((eye, i) => {
          const { left, top, width, height } = eye.getBoundingClientRect()
          const ex = left + width / 2
          const ey = top + height / 2
          
          if (i < 2) {
            eye.style.left = `${x*10+ex}px`
            eye.style.top = `${y*10+ey}px`
          } else {
            eye.style.left = `${x*10+ex}px`
            eye.style.top = `${y*10+ey}px`
          }
        })
      } catch { }
    }

    window.addEventListener('focus', handleFocus)
    return () => {
      window.removeEventListener('focus', handleFocus)
    }
  }, [])

  const covers = [...Array(4)].map((_, i) => (
    <span key={`cover-${i}`} className={`cover c${i}`} />
  ))

  const eyes = [...Array(4)].map((_, i) => (
    <span 
      key={`eye-${i}`}
      className={`eye e${i}`}
      ref={element => {
        if (!ref.current) ref.current = []
        if (element) ref.current[i] = element
      }}
    />
  ))

  return (
    <div className="Logo">
      <h1>
          seehoo
          {/* {covers}
          {eyes} */}
      </h1>
    </div>
  )
}

export default Logo
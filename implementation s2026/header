'use client';
import { useState } from 'react';
import Link from 'next/link';

const BLOG_LINKS = [
  { label: 'Christmas Nails', href: '/blog/christmas-nail-designs-2025' },
  { label: 'Seasonal Nails Ideas', href: '/topics/seasonal-trends' },
  { label: 'Nail Art Guide 2025', href: '/topics/nail-art-guides' },
  { label: 'Professional Women', href: '/topics/modern-women' },
  { label: 'Browse All Topics', href: '/topics' },
];

const SHOP_LINKS = [
  { label: 'Christmas Nails', href: '/shop/christmas' },
  { label: 'Winter Designs', href: '/shop/winter' },
  { label: 'Halloween Styles', href: '/shop/halloween' },
  { label: 'Trendy Collections', href: '/shop/trendy' },
  { label: 'View All Collections', href: '/shop' },
];

const DESIGNS_LINKS = [
  { label: 'Chrome Metallic Winter Nails', href: '/inspo/chrome-metallic-winter-nails' },
  { label: 'Burgundy Wine Winter Nails', href: '/inspo/burgundy-wine-winter-nails' },
  { label: 'Chocolate Brown Winter Nails', href: '/inspo/chocolate-brown-winter-nails' },
  { label: 'Velvet Cat Eye Winter Nails', href: '/inspo/velvet-cat-eye-winter-nails' },
  { label: 'View All Collections', href: '/inspo' },
];

const TOPICS_LINKS = [
  { label: 'Seasonal Trends', href: '/topics/seasonal-trends' },
  { label: 'Nail Art Guides', href: '/topics/nail-art-guides' },
  { label: 'Modern Women', href: '/topics/modern-women' },
  { label: 'Beauty Tips', href: '/topics/beauty-tips' },
  { label: 'Browse All Topics', href: '/topics' },
];

export default function Header() {
  return (
    <header className="bg-[#252220]">
      {/* Desktop Header */}
      <div className="hidden md:block">
        {/* Top Row - Newsletter, Work With Us, Search on Right */}
        <div className="border-b border-[#f9fafb]/20">
          <div className="container-standard mx-auto px-16">
            <div className="flex justify-center items-center h-16 relative">
              {/* Brand - Centered */}
              <Link href="/" className="flex items-center">
              <span 
                data-logo="true" 
                style={{ fontFamily: 'Larken, Georgia, serif' }} 
                className="text-3xl font-bold text-[#f9fafb]"
              >
                Mirellé
              </span>
              </Link>

              {/* Right Links */}
              <div className="flex items-center gap-6 absolute right-0">
                <a 
                  href="https://mirelleinspo.com/subscribe" 
                  style={{ fontFamily: 'General Sans, sans-serif' }}
                  className="text-xs tracking-widest uppercase text-[#f9fafb] hover:opacity-70 transition-opacity border border-[#f9fafb] px-4 py-2"
                >
                  NEWSLETTER
                </a>
                <Link 
                  href="/work-with-us"
                  style={{ fontFamily: 'General Sans, sans-serif' }}
                  className="text-xs tracking-widest uppercase text-[#f9fafb] hover:opacity-70 transition-opacity"
                >
                  WORK WITH US
                </Link>
              </div>
            </div>
          </div>
        </div>

        {/* Bottom Row - Main Navigation Links */}
        <nav className="border-b border-[#f9fafb]/20">
          <div className="container-standard mx-auto px-16">
            <div className="flex justify-center items-center h-12 gap-10">
              <Link 
                href="/"
                style={{ fontFamily: 'General Sans, sans-serif' }}
                className="text-sm tracking-wider uppercase text-[#f9fafb] hover:opacity-70 transition-opacity"
              >
                HOME
              </Link>
              <Link 
                href="/about"
                style={{ fontFamily: 'General Sans, sans-serif' }}
                className="text-sm tracking-wider uppercase text-[#f9fafb] hover:opacity-70 transition-opacity"
              >
                ABOUT
              </Link>
              
              {/* Blog Dropdown - Full Width Style */}
              <div className="relative group">
                <Link 
                  href="/blog"
                  style={{ fontFamily: 'General Sans, sans-serif' }}
                  className="text-sm tracking-wider uppercase text-[#f9fafb] hover:opacity-70 transition-opacity"
                >
                  BLOG
                </Link>
                <div className="fixed left-0 right-0 top-[7.5rem] opacity-0 invisible translate-y-2 group-hover:opacity-100 group-hover:visible group-hover:translate-y-0 transition-all duration-500 ease-out z-50">
                  <div className="bg-[#252220] border-b border-[#f9fafb]/20 shadow-2xl">
                    <div className="max-w-7xl mx-auto px-16 py-12">
                      <div className="space-y-1">
                        {BLOG_LINKS.map((link) => (
                          <Link
                            key={link.href}
                            href={link.href}
                            style={{ fontFamily: 'General Sans, sans-serif' }}
                            className="block py-3 text-lg text-[#f9fafb] hover:opacity-70 hover:pl-2 transition-all duration-300"
                          >
                            {link.label}
                          </Link>
                        ))}
                      </div>
                    </div>
                  </div>
                </div>
              </div>

              {/* Shop Dropdown - Full Width Style */}
              <div className="relative group">
                <Link 
                  href="/shop"
                  style={{ fontFamily: 'General Sans, sans-serif' }}
                  className="text-sm tracking-wider uppercase text-[#f9fafb] hover:opacity-70 transition-opacity"
                >
                  SHOP
                </Link>
                <div className="fixed left-0 right-0 top-[7.5rem] opacity-0 invisible translate-y-2 group-hover:opacity-100 group-hover:visible group-hover:translate-y-0 transition-all duration-500 ease-out z-50">
                  <div className="bg-[#252220] border-b border-[#f9fafb]/20 shadow-2xl">
                    <div className="max-w-7xl mx-auto px-16 py-12">
                      <div className="space-y-1">
                        {SHOP_LINKS.map((link) => (
                          <Link
                            key={link.href}
                            href={link.href}
                            style={{ fontFamily: 'General Sans, sans-serif' }}
                            className="block py-3 text-lg text-[#f9fafb] hover:opacity-70 hover:pl-2 transition-all duration-300"
                          >
                            {link.label}
                          </Link>
                        ))}
                      </div>
                    </div>
                  </div>
                </div>
              </div>

              {/* Designs Dropdown - Full Width Style */}
              <div className="relative group">
                <button 
                  style={{ fontFamily: 'General Sans, sans-serif' }}
                  className="text-sm tracking-wider uppercase text-[#f9fafb] hover:opacity-70 transition-opacity"
                >
                  DESIGNS
                </button>
                <div className="fixed left-0 right-0 top-[7.5rem] opacity-0 invisible translate-y-2 group-hover:opacity-100 group-hover:visible group-hover:translate-y-0 transition-all duration-500 ease-out z-50">
                  <div className="bg-[#252220] border-b border-[#f9fafb]/20 shadow-2xl">
                    <div className="max-w-7xl mx-auto px-16 py-12">
                      <div className="space-y-1">
                        {DESIGNS_LINKS.map((link) => (
                          <Link
                            key={link.href}
                            href={link.href}
                            style={{ fontFamily: 'General Sans, sans-serif' }}
                            className="block py-3 text-lg text-[#f9fafb] hover:opacity-70 hover:pl-2 transition-all duration-300"
                          >
                            {link.label}
                          </Link>
                        ))}
                      </div>
                    </div>
                  </div>
                </div>
              </div>

              {/* Topics Dropdown - Full Width Style */}
              <div className="relative group">
                <button 
                  style={{ fontFamily: 'General Sans, sans-serif' }}
                  className="text-sm tracking-wider uppercase text-[#f9fafb] hover:opacity-70 transition-opacity"
                >
                  TOPICS
                </button>
                <div className="fixed left-0 right-0 top-[7.5rem] opacity-0 invisible translate-y-2 group-hover:opacity-100 group-hover:visible group-hover:translate-y-0 transition-all duration-500 ease-out z-50">
                  <div className="bg-[#252220] border-b border-[#f9fafb]/20 shadow-2xl">
                    <div className="max-w-7xl mx-auto px-16 py-12">
                      <div className="space-y-1">
                        {TOPICS_LINKS.map((link) => (
                          <Link
                            key={link.href}
                            href={link.href}
                            style={{ fontFamily: 'General Sans, sans-serif' }}
                            className="block py-3 text-lg text-[#f9fafb] hover:opacity-70 hover:pl-2 transition-all duration-300"
                          >
                            {link.label}
                          </Link>
                        ))}
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </nav>
      </div>

      {/* Mobile Header */}
      <div className="md:hidden">
        {/* Top Row - Brand + Newsletter & Work With Us */}
        <div className="border-b border-[#f9fafb]/20">
          <div className="px-6 h-16 flex items-center justify-between">
            {/* Brand */}
            <Link href="/" className="flex items-center">
              <span style={{ fontFamily: 'Larken, Georgia, serif' }} className="text-2xl font-bold text-[#f9fafb]">
                Mirellé
              </span>
            </Link>

            {/* Right Side */}
            <div className="flex items-center gap-4">
              <a 
                href="https://mirelleinspo.com/subscribe"
                style={{ fontFamily: 'General Sans, sans-serif' }}
                className="text-[10px] tracking-wider uppercase text-[#f9fafb] hover:opacity-70 transition-opacity"
              >
                NEWSLETTER
              </a>
              <Link 
                href="/work-with-us"
                style={{ fontFamily: 'General Sans, sans-serif' }}
                className="text-[10px] tracking-wider uppercase text-[#f9fafb] hover:opacity-70 transition-opacity"
              >
                WORK WITH US
              </Link>
            </div>
          </div>
        </div>

        {/* Swipeable Navigation Row */}
        <div className="border-b border-[#f9fafb]/20 overflow-x-auto scrollbar-hide">
          <div className="flex gap-8 px-6 h-12 items-center whitespace-nowrap">
            <Link 
              href="/"
              style={{ fontFamily: 'General Sans, sans-serif' }}
              className="text-xs tracking-wider uppercase text-[#f9fafb] hover:opacity-70 transition-opacity"
            >
              HOME
            </Link>
            <Link 
              href="/about"
              style={{ fontFamily: 'General Sans, sans-serif' }}
              className="text-xs tracking-wider uppercase text-[#f9fafb] hover:opacity-70 transition-opacity"
            >
              ABOUT
            </Link>
            <Link 
              href="/blog"
              style={{ fontFamily: 'General Sans, sans-serif' }}
              className="text-xs tracking-wider uppercase text-[#f9fafb] hover:opacity-70 transition-opacity"
            >
              BLOG
            </Link>
            <Link 
              href="/shop"
              style={{ fontFamily: 'General Sans, sans-serif' }}
              className="text-xs tracking-wider uppercase text-[#f9fafb] hover:opacity-70 transition-opacity"
            >
              SHOP
            </Link>
            <Link 
              href="/inspo"
              style={{ fontFamily: 'General Sans, sans-serif' }}
              className="text-xs tracking-wider uppercase text-[#f9fafb] hover:opacity-70 transition-opacity"
            >
              DESIGNS
            </Link>
            <Link 
              href="/topics"
              style={{ fontFamily: 'General Sans, sans-serif' }}
              className="text-xs tracking-wider uppercase text-[#f9fafb] hover:opacity-70 transition-opacity"
            >
              TOPICS
            </Link>
          </div>
        </div>
      </div>

      <style jsx>{`
        .scrollbar-hide::-webkit-scrollbar {
          display: none;
        }
        .scrollbar-hide {
          -ms-overflow-style: none;
          scrollbar-width: none;
        }
      `}</style>
    </header>
  );
}

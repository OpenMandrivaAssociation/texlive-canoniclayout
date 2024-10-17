Name:		texlive-canoniclayout
Epoch:		1
Version:	64889
Release:	2
Summary:	Create canonical page layouts with memoir
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/canoniclayout
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/canoniclayout.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/canoniclayout.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/canoniclayout.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A canonic text layout has specified relations to a circle
inscribed within the enclosing page. The package allows the
user to use a canonic layout with the memoir class.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/canoniclayout
%doc %{_texmfdistdir}/doc/latex/canoniclayout
#- source
%doc %{_texmfdistdir}/source/latex/canoniclayout

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}

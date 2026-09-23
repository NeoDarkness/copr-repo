%global debug_package %{nil}

%global __provides_exclude_from ^/opt/Postman/.*$
%global __requires_exclude_from ^/opt/Postman/.*$

Name:           postman
Version:        12.29.2
Release:        %autorelease
Summary:        Postman API Platform

License:        Proprietary
URL:            https://www.postman.com/

Source0:        https://dl.pstmn.io/download/version/%{version}/linux64
Source1:        postman.desktop

ExclusiveArch:  x86_64

Provides:       bundled(electron)
Provides:       bundled(ffmpeg)
Provides:       bundled(vulkan-loader)

%description
Build, test, and document your APIs faster.

%prep
%autosetup -n Postman

%build

%install
install -d %{buildroot}/opt/Postman
cp -a * %{buildroot}/opt/Postman/

install -d %{buildroot}%{_bindir}
ln -sr %{buildroot}/opt/Postman/Postman %{buildroot}%{_bindir}/postman

install -Dpm 0644 %{SOURCE1} \
    %{buildroot}%{_datadir}/applications/postman.desktop

install -Dpm 0644 \
    %{buildroot}/opt/Postman/app/resources/app/assets/icon.png \
    %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/postman.png

%check

%files
/opt/Postman
%{_bindir}/postman
%{_datadir}/applications/postman.desktop
%{_datadir}/icons/hicolor/128x128/apps/postman.png

%changelog
%autochangelog